import click

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import scipy.sparse as ss
from sklearn import linear_model, metrics
from sklearn.neighbors import NearestNeighbors
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor


from .poisson import PoissonRegression
from .data import rmse, mape, laplacian_embedding, create_dataset
import pdb


def plot_top(y, y_pred):
    """Creates a 2x4 plot of individual series with prediction overlay."""
    plt.figure(figsize=(16, 6))
    for i in range(8):
        plt.subplot(2, 4, i + 1)
        plt.plot(y[i].T, label="y")
        plt.plot(y_pred[i].T, label="$\hat{y}$")
        plt.legend()


def summarize(model_name, y, y_pred):
    print(f"{mape(y, y_pred):.2e}\t{rmse(y, y_pred):.2e}\t{model_name}")


def plot_scree(g, k=64):
    L = nx.laplacian_matrix(g).astype("float64")
    w, v = ss.linalg.eigsh(L, k=k)
    plt.title("scree plot of laplacian eigenvalues")
    plt.plot(np.arange(k), w[::-1])


def run_ablation(name, model, train, validate, test, pagerank, emb, **kwargs):
    test_X = np.hstack([train[:, 7:], validate])

    z = np.hstack([train, pagerank, emb])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X, pagerank, emb])
    summarize(f"{name}: history + pagerank + emb", test, model.predict(z))

    z = np.hstack([train, pagerank])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X, pagerank])
    summarize(f"{name}: history + pagerank", test, model.predict(z))

    z = np.hstack([train, emb])
    model.fit(train, validate, **kwargs)
    z = np.hstack([test_X, emb])
    summarize(f"{name}: history + emb", test, model.predict(test_X))

    z = np.hstack([train[:, -7:], pagerank, emb])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X[:, -7:], pagerank, emb])
    summarize(f"{name}: pagerank + emb", test, model.predict(z))

    z = np.hstack([train])
    model.fit(train, validate, **kwargs)
    z = np.hstack([test_X])
    summarize(f"{name}: history", test, model.predict(test_X))

    z = np.hstack([train[:, -7:], pagerank])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X[:, -7:], pagerank])
    summarize(f"{name}: pagerank", test, model.predict(z))

    z = np.hstack([train[:, -7:], emb])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X[:, -7:], emb])
    summarize(f"{name}: emb", test, model.predict(z))

    model.fit(train[:, -7:], validate, **kwargs)
    summarize(f"{name}: baseline", test, model.predict(test_X[:, -7:]))


def weighted_linear_regression(train, validate, test, pagerank, emb):
    train_X = train[:, -7:]
    test_X = np.hstack([validate])

    def run(name, weights):
        # weights needs to be a 1d array
        model = linear_model.Ridge(alpha=0)

        z = np.hstack([train_X, pagerank, emb])
        model.fit(z, validate, weights)
        z = np.hstack([test_X, pagerank, emb])
        summarize(
            f"weighted linear regression ({name}): pagerank + emb",
            test,
            model.predict(z),
        )

        z = np.hstack([train_X, pagerank])
        model.fit(z, validate, weights)
        z = np.hstack([test_X, pagerank])
        summarize(
            f"weighted linear regression ({name}): pagerank", test, model.predict(z)
        )

        # weights needs to be a 1d array
        z = np.hstack([train_X, emb])
        model.fit(z, validate, weights)
        z = np.hstack([test_X, emb])
        summarize(f"weighted linear regression ({name}): emb", test, model.predict(z))

        model.fit(train_X, validate, weights)
        summarize(
            f"weighted linear regression ({name}): baseline",
            test,
            model.predict(test_X),
        )

    run("pagerank", pagerank.T[0])

    # the L2-norm of the average embedding over k-nearest neighbors
    # TODO: test over different parameters of
    tree = NearestNeighbors(n_neighbors=10, algorithm="ball_tree").fit(emb)
    _, ind = tree.kneighbors(emb)
    weights = np.linalg.norm(emb[ind[:, 1:]].mean(axis=1), axis=1)

    model = linear_model.Ridge(alpha=0)
    model.fit(train, validate, weights)
    summarize("weighted regression (avg emb)", test, model.predict(test_X))


def poisson_regression(train, validate, test, pagerank, emb):
 
    # Poisson model with the embedding as feature     
    model = PoissonRegression()
    model.fit(emb, validate)
    summarize("poisson regression emb", test, model.predict(emb))

    # Poisson model with pagerank + embedding as feature
    model = PoissonRegression()
    z = np.hstack([pagerank, emb])
    model.fit(z, validate)
    summarize("poisson regression pagerank + emb", test, model.predict(z))


def run_trial(mapping, edges, ts):
    embedding_size = 8
    window_size = 7
    num_windows = 54

    train, validate, test = create_dataset(ts, window_size, num_windows)
    print(f"train shape: {train.shape}")
    print(f"validate shape: {validate.shape}")
    print(f"test shape: {test.shape}")

    g = nx.subgraph(
        nx.from_pandas_edgelist(
            edges, source="src", target="dst", create_using=nx.Graph
        ),
        ts.id,
    )
    print(nx.info(g))
    plot_scree(g)
    plt.show()
    emb = laplacian_embedding(g, embedding_size)

    # (n,1) column so it can be stacked using hstack
    pagerank = np.array([ts.merge(mapping).pagerank.values]).T

    print("MAPE\tRMSE\tmodel name")
    summarize("persistence", test, validate)
    summarize("mean", test, (np.ones(test.shape).T * validate.mean(axis=1)).T)

    model = linear_model.LinearRegression()
    run_ablation("linear regression", model, train, validate, test, pagerank, emb)

    # custom ablation
    weighted_linear_regression(train, validate, test, pagerank, emb)
    poisson_regression(train, validate, test, pagerank, emb)

    model = DecisionTreeRegressor()
    run_ablation("decision tree", model, train, validate, test, pagerank, emb)


@click.command()
@click.option("--mapping-path", default="sample_data/trial_6/mapping.csv")
@click.option("--edges-path", default="sample_data/trial_6/edges.csv")
@click.option("--ts-path", default="sample_data/trial_6/ts.csv")
def main(mapping_path, edges_path, ts_path):
    """Run experiments on a sampled graph that fits into memory"""
    mapping = pd.read_csv(mapping_path)
    edges = pd.read_csv(edges_path)
    ts = pd.read_csv(ts_path)
    run_trial(mapping, edges, ts)
