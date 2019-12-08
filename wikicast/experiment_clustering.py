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


def run_trial(data, output, window_size, num_windows):
    train, validate, test = create_dataset(data[DATES], window_size, num_windows)
    features = [data[DEGREE].values, data[SIGN].values, data[VECTOR].values]
    features_dict = dict(zip(["degree", "sign", "vector"], features))

    print(f"train shape: {train.shape}")
    print(f"validate shape: {validate.shape}")
    print(f"test shape: {test.shape}")

    results = [
        summarize("persistence", test, validate),
        summarize("mean", test, (np.ones(test.shape).T * validate.mean(axis=1)).T),
    ]

    pred = run_train_predict(Ridge(alpha=0), train, validate, test, [])
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
        "ridge regression", search_ridge, train, validate, test, features_dict
    )
    write_search_results(search_ridge, f"{output}/ridge-random.csv")

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
        search.fit(np.hstack([train] + features), validate)
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
        search.fit(np.hstack([train] + features), validate)
        write_search_results(search, output)
        return search

    # 30 trials, should be reduced to 8 trials
    layers = [(16, 16), (64, 128), (128, 8, 128), (64, 32, 8), (16, 8, 8, 8)]
    params = {
        "learning_rate_init": [3e-5, 8e-5],
        "activation": ["relu"],
        "hidden_layer_sizes": layers,
        "alpha": [5e5, 5e4, 0.5],
    }
    search = best_nn_grid(params, f"{output}/nn-grid-layers-best.csv")

    best_nn = search.best_estimator_
    results += run_ablation(
        "neural network", best_nn, train, validate, test, features_dict
    )

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

    df = pd.read_parquet(glob.glob(design_path)[0]).fillna(0)
    pretty_columns = META + DEGREE + SIGN[:1] + VECTOR[:1] + DATES[:3]
    print(df.shape)
    print(df.loc[:, pretty_columns].sample(5))

    sample_size = 1 * 10 ** 4
    run_trial(df.sample(sample_size), output_path, window_size, num_windows)


if __name__ == "__main__":
    main()
