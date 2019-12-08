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
from .data import (
    rmse,
    mape,
    laplacian_embedding,
    create_dataset,
    create_rolling_datasets,
)


def plot_top(y, y_pred):
    """Creates a 2x4 plot of individual series with prediction overlay."""
    plt.figure(figsize=(16, 6))
    for i in range(8):
        plt.subplot(2, 4, i + 1)
        plt.plot(y[i].T, label="y")
        plt.plot(y_pred[i].T, label="$\hat{y}$")
        plt.legend()


def summarize(model_name, y, y_pred, trial_id=1):
    """Return a dictionary of results"""
    return {
        "mape": mape(y, y_pred),
        "rmse": rmse(y, y_pred),
        "name": model_name,
        "trial_id": trial_id,
    }


def plot_scree(g, k=64):
    L = nx.laplacian_matrix(g).astype("float64")
    w, v = ss.linalg.eigsh(L, k=k)
    plt.title("scree plot of laplacian eigenvalues")
    plt.plot(np.arange(k), w[::-1])


def run_ablation(
    name, model, train, validate, test, pagerank, emb, trial_id=-1, **kwargs
):
    results = []
    test_X = np.hstack([train[:, 7:], validate])

    z = np.hstack([train, pagerank, emb])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X, pagerank, emb])
    results.append(
        summarize(
            f"{name}: history + pagerank + emb",
            test,
            model.predict(z),
            trial_id=trial_id,
        )
    )

    z = np.hstack([train, pagerank])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X, pagerank])
    results.append(
        summarize(
            f"{name}: history + pagerank", test, model.predict(z), trial_id=trial_id
        )
    )

    z = np.hstack([train, emb])
    model.fit(train, validate, **kwargs)
    z = np.hstack([test_X, emb])
    results.append(
        summarize(
            f"{name}: history + emb", test, model.predict(test_X), trial_id=trial_id
        )
    )

    z = np.hstack([train[:, -7:], pagerank, emb])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X[:, -7:], pagerank, emb])
    results.append(
        summarize(f"{name}: pagerank + emb", test, model.predict(z), trial_id=trial_id)
    )

    z = np.hstack([train])
    model.fit(train, validate, **kwargs)
    z = np.hstack([test_X])
    results.append(
        summarize(f"{name}: history", test, model.predict(test_X), trial_id=trial_id)
    )

    z = np.hstack([train[:, -7:], pagerank])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X[:, -7:], pagerank])
    results.append(
        summarize(f"{name}: pagerank", test, model.predict(z), trial_id=trial_id)
    )

    z = np.hstack([train[:, -7:], emb])
    model.fit(z, validate, **kwargs)
    z = np.hstack([test_X[:, -7:], emb])
    results.append(summarize(f"{name}: emb", test, model.predict(z), trial_id))

    model.fit(train[:, -7:], validate, **kwargs)
    results.append(
        summarize(
            f"{name}: baseline", test, model.predict(test_X[:, -7:]), trial_id=trial_id
        )
    )
    return results


def weighted_linear_regression(train, validate, test, pagerank, emb, trial_id=1):
    train_X = train[:, -7:]
    test_X = np.hstack([validate])

    def run(name, weights, trial_id=1):
        results = []
        # weights needs to be a 1d array
        model = linear_model.Ridge(alpha=0)

        z = np.hstack([train_X, pagerank, emb])
        model.fit(z, validate, weights)
        z = np.hstack([test_X, pagerank, emb])
        results.append(
            summarize(
                f"weighted linear regression ({name}): pagerank + emb",
                test,
                model.predict(z),
                trial_id=trial_id,
            )
        )

        z = np.hstack([train_X, pagerank])
        model.fit(z, validate, weights)
        z = np.hstack([test_X, pagerank])
        results.append(
            summarize(
                f"weighted linear regression ({name}): pagerank",
                test,
                model.predict(z),
                trial_id=trial_id,
            )
        )

        # weights needs to be a 1d array
        z = np.hstack([train_X, emb])
        model.fit(z, validate, weights)
        z = np.hstack([test_X, emb])
        results.append(
            summarize(
                f"weighted linear regression ({name}): emb",
                test,
                model.predict(z),
                trial_id=trial_id,
            )
        )

        model.fit(train_X, validate, weights)
        results.append(
            summarize(
                f"weighted linear regression ({name}): baseline",
                test,
                model.predict(test_X),
                trial_id=trial_id,
            )
        )
        return results

    pr_results = run("pagerank", pagerank.T[0], trial_id=trial_id)

    # the L2-norm of the average embedding over k-nearest neighbors
    # TODO: test over different parameters of
    tree = NearestNeighbors(n_neighbors=10, algorithm="ball_tree").fit(emb)
    _, ind = tree.kneighbors(emb)
    weights = np.linalg.norm(emb[ind[:, 1:]].mean(axis=1), axis=1)

    emb_results = run("avg emb", weights, trial_id=trial_id)
    return pr_results + emb_results


def normalized_linear_regression(ts, window_size, num_windows, **kwargs):
    results = []
    trial_id = kwargs["trial_id"]
    del kwargs["trial_id"]
    train, validate, test = create_dataset(ts, window_size, num_windows)
    model = linear_model.LinearRegression()

    # avoid normalizing the output variables, otherwise the true prediction
    # can't be recovered
    normalize = lambda x: (x - train.mean()) / (train.max() - train.min())
    test_X = np.hstack([train[:, 7:], validate])
    model.fit(normalize(train), validate, **kwargs)
    results.append(
        summarize(
            f"linear regresson, history only, normalized data",
            test,
            model.predict(normalize(test_X)),
            trial_id=trial_id,
        )
    )
    return results


def run_rolling_trials(mapping, edges, ts, plot_scree=False):
    embedding_size = 8
    window_size = 7
    num_windows = 54

    datasets = create_rolling_datasets(ts, window_size, num_windows)

    results = []

    g = nx.subgraph(
        nx.from_pandas_edgelist(
            edges, source="src", target="dst", create_using=nx.Graph
        ),
        ts.id,
    )
    print(nx.info(g))
    if plot_scree:
        plot_scree(g)
        plt.show()
    emb = laplacian_embedding(g, embedding_size)

    for window, dataset in enumerate(datasets):

        print("Running on Window {}".format(window))

        train = dataset["train"]
        validate = dataset["validate"]
        test = dataset["test"]

        pagerank = np.array([ts.merge(mapping).pagerank.values]).T

        window_results = [
            summarize("persistence", test, validate),
            summarize("mean", test, (np.ones(test.shape).T * validate.mean(axis=1)).T),
        ]

        model = linear_model.LinearRegression()
        window_results += run_ablation(
            "linear regression", model, train, validate, test, pagerank, emb
        )

        # custom ablation
        weighted_linear_regression(train, validate, test, pagerank, emb)

        model = DecisionTreeRegressor()
        window_results += run_ablation(
            "decision tree", model, train, validate, test, pagerank, emb
        )

        for result in window_results:
            result["window"] = window

        results += window_results

    return results


def run_trial(mapping, edges, ts, plot_scree=False, trial_id=1):
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
    if plot_scree:
        plot_scree(g)
        plt.show()
    emb = laplacian_embedding(g, embedding_size)

    # (n,1) column so it can be stacked using hstack
    pagerank = np.array([ts.merge(mapping).pagerank.values]).T

    results = [
        summarize("persistence", test, validate, trial_id=trial_id),
        summarize(
            "mean",
            test,
            (np.ones(test.shape).T * validate.mean(axis=1)).T,
            trial_id=trial_id,
        ),
    ]

    model = linear_model.LinearRegression()
    results += run_ablation(
        "linear regression",
        model,
        train,
        validate,
        test,
        pagerank,
        emb,
        trial_id=trial_id,
    )

    # run poisson,
    poisson = PoissonRegression()
    poisson.fit(train.mean(axis=1, keepdims=True), validate)
    results += [
        summarize(
            "poisson",
            test,
            poisson.predict(
                np.hstack([train[:, 7:], validate]).mean(axis=1, keepdims=True)
            ),
            trial_id=trial_id,
        )
    ]

    # custom ablation
    weighted_linear_regression(train, validate, test, pagerank, emb, trial_id=trial_id)

    results += normalized_linear_regression(
        ts, window_size, num_windows, trial_id=trial_id
    )

    model = DecisionTreeRegressor()
    results += run_ablation(
        "decision tree", model, train, validate, test, pagerank, emb, trial_id=trial_id
    )

    return results


@click.command()
@click.option("--mapping-path", default="sample_data/trial_6/mapping.csv")
@click.option("--edges-path", default="sample_data/trial_6/edges.csv")
@click.option("--ts-path", default="sample_data/trial_6/ts.csv")
@click.option("--rolling-validation/--no-rolling-validation", default=False)
def main(mapping_path, edges_path, ts_path, rolling_validation):
    """Run experiments on a sampled graph that fits into memory"""
    pd.set_option("display.max_colwidth", -1)

    mapping = pd.read_csv(mapping_path)
    edges = pd.read_csv(edges_path)
    ts = pd.read_csv(ts_path)
    if rolling_validation:
        results = run_rolling_trials(mapping, edges, ts)
        results_df = pd.DataFrame(results)[["window", "name", "mape", "rmse"]]
        results_df.to_csv(path_or_buf="results.csv", index=False)
    else:
        results = run_trial(mapping, edges, ts)
        print(pd.DataFrame(results)[["trial_id", "name", "mape", "rmse"]])


if __name__ == "__main__":
    main()
