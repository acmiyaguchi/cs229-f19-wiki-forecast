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

from .data import rmse, mape, laplacian_embedding, create_dataset


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


def linear_regression(train, validate, test, pagerank, emb):
    test_X = np.hstack([train[:, 7:], validate])

    model = linear_model.LinearRegression()
    model.fit(train, validate)
    summarize("linear regression", test, model.predict(test_X))

    model = linear_model.LinearRegression()
    z = np.hstack([train, pagerank])
    model.fit(z, validate)
    z = np.hstack([test_X, pagerank])
    summarize("linear regression + pagerank", test, model.predict(z))

    model = linear_model.LinearRegression()
    z = np.hstack([train, emb])
    model.fit(z, validate)
    z = np.hstack([test_X, emb])
    summarize("linear regression + emb", test, model.predict(z))


def weighted_linear_regression(train, validate, test, pagerank, emb):
    test_X = np.hstack([train[:, 7:], validate])

    # weights needs to be a 1d array
    model = linear_model.Ridge(alpha=0)
    model.fit(train, validate, pagerank.T[0])
    summarize("weighted linear regression (pagerank)", test, model.predict(test_X))

    # the L2-norm of the average embedding over k-nearest neighbors
    # TODO: test over different parameters of
    tree = NearestNeighbors(n_neighbors=10, algorithm="ball_tree").fit(emb)
    _, ind = tree.kneighbors(emb)
    weights = np.linalg.norm(emb[ind[:, 1:]].mean(axis=1), axis=1)

    model = linear_model.Ridge(alpha=0)
    model.fit(train, validate, weights)
    summarize("weighted regression (avg emb)", test, model.predict(test_X))


def decision_tree(train, validate, test, pagerank, emb):
    test_X = np.hstack([train[:, 7:], validate])

    model = DecisionTreeRegressor()
    model.fit(train, validate)
    summarize("decision tree", test, model.predict(test_X))

    model = DecisionTreeRegressor()
    z = np.hstack([train, emb])
    model.fit(z, validate)
    z = np.hstack([test_X, emb])
    summarize("decision tree + emb", test, model.predict(z))


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
    emb = laplacian_embedding(g, 8)

    # (n,1) column so it can be stacked using hstack
    pagerank = np.array([ts.merge(mapping).pagerank.values]).T

    print("MAPE\tRMSE\tmodel name")
    summarize("persistence", test, validate)
    summarize("mean", test, (np.ones(test.shape).T * validate.mean(axis=1)).T)
    linear_regression(train, validate, test, pagerank, emb)
    weighted_linear_regression(train, validate, test, pagerank, emb)
    decision_tree(train, validate, test, pagerank, emb)


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
