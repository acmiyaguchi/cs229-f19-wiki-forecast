from itertools import chain, product
from time import time

import click
import networkx as nx
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.linear_model import Ridge
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.neural_network import MLPRegressor

from .baseline import run_ablation, summarize
from .data import create_dataset, laplacian_embedding, mape, rmse


def write_results(search, output):
    df = pd.DataFrame(search.cv_results_).sort_values("rank_test_rmse")
    df.to_csv(output)
    params = [c for c in df.columns if c.startswith("param_")]
    view_cols = [
        "mean_test_rmse",
        "mean_test_mape",
        "rank_test_rmse",
        "rank_test_mape",
        "mean_fit_time",
    ] + params
    print(df[view_cols])
    return df


def run_trial(mapping, edges, ts, output_path="data/results", search_layer_sizes=False):
    embedding_size = 32
    window_size = 7
    num_windows = 120 // window_size

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
    emb = laplacian_embedding(g, embedding_size)
    pagerank = np.array([ts.merge(mapping).pagerank.values]).T

    results = [
        summarize("persistence", test, validate),
        summarize("mean", test, (np.ones(test.shape).T * validate.mean(axis=1)).T),
    ]

    linreg = Ridge(alpha=0)
    linreg.fit(train, validate)
    test_X = np.hstack([train[:, window_size:], validate])
    pred = linreg.predict(test_X)
    results += [summarize("linear regression", test, pred)]

    scoring = {
        "rmse": make_scorer(rmse, greater_is_better=False),
        "mape": make_scorer(mape, greater_is_better=False),
    }

    ridge = Ridge()
    params = dict(alpha=stats.reciprocal(a=1e-2, b=1e8))
    search_ridge = RandomizedSearchCV(
        estimator=ridge,
        param_distributions=params,
        scoring=scoring,
        refit="rmse",
        cv=5,
        n_iter=20,
        return_train_score=False,
    )
    results += run_ablation(
        "ridge regression", search_ridge, train, validate, test, pagerank, emb
    )
    write_results(search_ridge, f"{output_path}/ridge-random.csv")

    # closes over: train, pagerank, emb, validate, scoring
    def best_nn_grid(params, output, **kwargs):
        print(f"running for {output}")
        nn = MLPRegressor(solver="lbfgs")
        search = GridSearchCV(
            estimator=nn,
            param_grid=params,
            scoring=scoring,
            refit="rmse",
            cv=5,
            n_jobs=-1,
            return_train_score=False,
            **kwargs,
        )
        search.fit(np.hstack([train, pagerank, emb]), validate)
        write_results(search, output)
        return search

    def best_nn_random(params, output, **kwargs):
        print(f"running for {output}")
        nn = MLPRegressor(solver="lbfgs")
        search = RandomizedSearchCV(
            estimator=nn,
            param_distributions=params,
            scoring=scoring,
            refit="rmse",
            cv=5,
            n_jobs=-1,
            return_train_score=False,
            **kwargs,
        )
        search.fit(np.hstack([train, pagerank, emb]), validate)
        write_results(search, output)
        return search

    layers = [10, 100]
    params = {"activation": ["relu", "tanh"], "hidden_layer_sizes": layers}
    best_nn_grid(params, f"{output_path}/nn-activation.csv")

    layers = [10, 50, 100, 500]
    params = {"activation": ["relu"], "hidden_layer_sizes": layers}
    best_nn_grid(params, f"{output_path}/nn-grid-layers-1.csv")

    layers = [10, 50, 100]
    params = {
        "activation": ["relu"],
        "hidden_layer_sizes": list(chain(product(layers, repeat=2))),
    }
    best_nn_grid(params, f"{output_path}/nn-grid-layers-2.csv")

    if search_layer_sizes:
        params = {
            "activation": ["relu"],
            "hidden_layer_sizes": list(chain(product(layers, repeat=3))),
        }
        best_nn_grid(params, f"{output_path}/nn-grid-layers-3.csv")

        params = {
            "activation": ["relu"],
            "hidden_layer_sizes": list(chain(product(layers[:2], repeat=4))),
        }
        best_nn_grid(params, f"{output_path}/nn-grid-layers-4.csv")

        params = {
            "activation": ["relu"],
            "hidden_layer_sizes": list(chain(product(layers[:2], repeat=5))),
        }
        best_nn_random(params, f"{output_path}/nn-grid-layers-5-rnd.csv", n_iter=20)

        params = {
            "activation": ["relu"],
            "hidden_layer_sizes": list(chain(product(layers[:2], repeat=6))),
        }
        best_nn_random(params, f"{output_path}/nn-grid-layers-6-rnd.csv", n_iter=20)

        params = {
            "activation": ["relu"],
            "hidden_layer_sizes": list(chain(product(layers[:2], repeat=7))),
        }
        best_nn_random(params, f"{output_path}/nn-grid-layers-7-rnd.csv", n_iter=20)

    # 4-6 layers is best
    layers = [(10, 50, 10, 50, 10), (10, 10, 50, 10, 50, 10)]
    params = {
        "activation": ["relu"],
        "hidden_layer_sizes": layers,
        "alpha": [0.017, 0.07, 0.001, 0.1],
    }
    search = best_nn_grid(params, f"{output_path}/nn-grid-layers-alpha-best.csv")

    best_nn = search.best_estimator_
    results += run_ablation(
        "neural network", best_nn, train, validate, test, pagerank, emb
    )

    print(pd.DataFrame(results))
    return results


@click.command()
@click.option("--mapping-path", default="sample_data/trial_6/mapping.csv")
@click.option("--edges-path", default="sample_data/trial_6/edges.csv")
@click.option("--ts-path", default="sample_data/trial_6/ts.csv")
def main(mapping_path, edges_path, ts_path):
    """Run experiments on a sampled graph that fits into memory"""
    # TODO ensure data/results exists
    mapping = pd.read_csv(mapping_path)
    edges = pd.read_csv(edges_path)
    ts = pd.read_csv(ts_path)
    run_trial(mapping, edges, ts)


if __name__ == "__main__":
    main()
