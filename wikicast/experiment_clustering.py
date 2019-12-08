import glob
from datetime import datetime, timedelta
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

from .data import create_dataset, mape, rmse
from .util import run_ablation, run_train_predict, summarize, write_search_results

N_CUTS = 8
START_DATE = datetime.strptime("2018-01-01", "%Y-%m-%d")
END_DATE = datetime.strptime("2019-09-01", "%Y-%m-%d")

META = ["partition_id", "title"]
DEGREE = ["degree", "inDegree", "outDegree"]
SIGN = [f"sign_{i}" for i in range(N_CUTS)]
VECTOR = [f"fiedler_{i}" for i in range(N_CUTS)]
DATES = [
    (START_DATE + timedelta(t)).strftime("%Y-%m-%d")
    for t in range((END_DATE - START_DATE).days)
]

SCHEMA = META + DEGREE + SIGN + VECTOR + DATES


def run_trial(df, output_path, window_size, num_windows, sample_size=5 * 10 ** 4):
    data = df.fillna(0).sample(sample_size)


    train, validate, test = create_dataset(data[DATES], window_size, num_windows)
    print(f"train shape: {train.shape}")
    print(f"validate shape: {validate.shape}")
    print(f"test shape: {test.shape}")

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
    write_search_results(search_ridge, f"{output_path}/ridge-random.csv")

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
        write_search_results(search, output)
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

    # layers = [10, 100]
    # params = {"activation": ["relu", "tanh"], "hidden_layer_sizes": layers}
    # best_nn_grid(params, f"{output_path}/nn-activation.csv")

    # layers = [10, 50, 100, 500]
    # params = {"activation": ["relu"], "hidden_layer_sizes": layers}
    # best_nn_grid(params, f"{output_path}/nn-grid-layers-1.csv")

    # layers = [10, 50, 100]
    # params = {
    #     "activation": ["relu"],
    #     "hidden_layer_sizes": list(chain(product(layers, repeat=2))),
    # }
    # best_nn_grid(params, f"{output_path}/nn-grid-layers-2.csv")

    # 4-6 layers is best
    # layers = [(10, 50, 10, 50, 10), (10, 10, 50, 10, 50, 10)]
    # params = {
    #     "activation": ["relu"],
    #     "hidden_layer_sizes": layers,
    #     "alpha": [0.017, 0.07, 0.001, 0.1],
    # }
    # search = best_nn_grid(params, f"{output_path}/nn-grid-layers-alpha-best.csv")

    # best_nn = search.best_estimator_
    # results += run_ablation(
    #     "neural network", best_nn, train, validate, test, pagerank, emb
    # )

    print(pd.DataFrame(results))
    return results


@click.command()
@click.option(
    "--design-path",
    default="data/design_matrix/sample_6_8_50/*.parquet",
    help="path (include globs) to the design matrix",
)
@click.option(
    "--output-path",
    type=click.Path(exists=True, file_okay=False),
    default="data/results/experiment_clustering",
)
def main(design_path, output_path):
    """Run experiments on a sampled graph that fits into memory"""
    window_size = 7
    num_windows = 120 // window_size

    df = pd.read_parquet(glob.glob(design_path)[0])
    pretty_columns = META + DEGREE + SIGN[:1] + VECTOR[:1] + DATES[:3]
    print(df.shape)
    print(df.loc[:, pretty_columns].sample(5))

    run_trial(df, output_path, window_size, num_windows)


if __name__ == "__main__":
    main()
