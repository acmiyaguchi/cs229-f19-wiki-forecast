import glob
from datetime import datetime, timedelta
from itertools import chain, product
from time import time
import warnings

import click
import networkx as nx
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.neural_network import MLPRegressor

from .data import create_dataset, mape, rmse
from .util import (
    run_ablation,
    run_train_predict,
    summarize,
    write_search_results,
    plot_learning_curve,
)

# Turn off warning in this experiment
# FutureWarning: The default value of multioutput (not exposed in score method)
# will change from 'variance_weighted' to 'uniform_average' in 0.23 to keep
# consistent with 'metrics.r2_score'. To specify the default value manually and
# avoid the warning, please either call 'metrics.r2_score' directly or make a
# custom scorer with 'metrics.make_scorer' (the built-in scorer 'r2' uses
# multioutput='uniform_average').
warnings.filterwarnings("ignore")


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
    scaler = StandardScaler()
    features = [
        data[DEGREE].values,
        data[SIGN].values,
        scaler.fit_transform(data[VECTOR].values),
    ]
    features_dict = dict(zip(["degree", "sign", "vector"], features))

    print(f"train shape: {train.shape}")
    print(f"validate shape: {validate.shape}")
    print(f"test shape: {test.shape}")

    results = [
        summarize("persistence", test, validate),
        summarize("mean", test, (np.ones(test.shape).T * validate.mean(axis=1)).T),
    ]

    pred = run_train_predict(Ridge(alpha=0), train[:, -window_size:], validate, test, [])
    results += [summarize("linear regression (no history)", test, pred)]

    scoring = {
        "rmse": make_scorer(rmse, greater_is_better=False),
        "mape": make_scorer(mape, greater_is_better=False),
    }

    print("starting ridge")
    ridge = Ridge(solver="lsqr", alpha=1.8e8)
    # params = dict(alpha=stats.reciprocal(a=1e5, b=1e9))
    # search_ridge = RandomizedSearchCV(
    #     estimator=ridge,
    #     param_distributions=params,
    #     scoring=scoring,
    #     refit="rmse",
    #     cv=5,
    #     n_iter=5,
    #     return_train_score=False,
    # )
    search_ridge = ridge
    results += run_ablation(
        "ridge regression", search_ridge, train, validate, test, features_dict
    )
    # write_search_results(search_ridge, f"{output}/ridge-random.csv")

    # use lbfgs when the dataset is small, does not require a learning rate
    solver = "adam"

    def best_nn_grid(params, output, **kwargs):
        print(f"running for {output}")
        nn = MLPRegressor(solver=solver, early_stopping=True)
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
        nn = MLPRegressor(solver=solver, early_stopping=True)
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
    # layers = [(16, 16), (64, 128), (128, 8, 128), (64, 32, 8), (16, 8, 8, 8)]
    # params = {
    #     "learning_rate_init": [3e-5, 8e-5],
    #     "activation": ["relu"],
    #     "hidden_layer_sizes": layers,
    #     "alpha": [5e5, 5e4, 0.5],
    # }
    layers = [(64, 32, 64, 16)]
    params = {
        "hidden_layer_sizes": layers,
        "alpha": [0.002, 20],
    }
    search = best_nn_grid(params, f"{output}/nn-grid-regularization.csv")

    # layers = [
    #     #np.hstack([train] + features).shape[1],
    #     #(128, 8, 128),
    #     #(16, 8, 8, 8),
    #     (64, 32, 64, 16),
    # ]
    # params = {"hidden_layer_sizes": layers, "alpha": stats.reciprocal(1e-4, 1e2)}
    # search = best_nn_random(params, f"{output}/nn-grid-layers-best.csv", n_iter=10)

    best_nn = search.best_estimator_
    results += run_ablation(
        "neural network", best_nn, train, validate, test, features_dict
    )

    plot_learning_curve(
        best_nn, np.hstack([train] + features), validate, f"{output}/learning_curve.png"
    )

    print(pd.DataFrame(results))
    return results


@click.command()
@click.option(
    "--design-path",
    default="data/design_matrix/sample_3_8_50/*.parquet",
    help="path (include globs) to the design matrix",
)
@click.option(
    "--output-path",
    type=click.Path(exists=True, file_okay=False),
    default="data/results/experiment_clustering",
)
@click.option("--sample-ratio", type=float, default=0.10)
def main(design_path, output_path, sample_ratio):
    """Run experiments on a sampled graph that fits into memory"""
    window_size = 7
    num_windows = 60

    df = pd.read_parquet(glob.glob(design_path)[0]).fillna(0)
    pretty_columns = META + DEGREE + SIGN[:1] + VECTOR[:1] + DATES[:3]
    print(df.shape)
    print(df.loc[:, pretty_columns].sample(5))

    start = time()
    sample_size = int(df.shape[0] * sample_ratio)
    results = run_trial(df.sample(sample_size), output_path, window_size, num_windows)
    pd.DataFrame(results).to_csv(f"{output_path}/results.csv")
    print(f"took {time()-start} seconds!")


if __name__ == "__main__":
    main()
