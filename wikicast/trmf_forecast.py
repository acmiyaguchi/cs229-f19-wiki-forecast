#!/usr/bin/env python
import pandas as pd
import scipy as sp
import trmf
from datetime import datetime, timedelta

import itertools

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

def run_trial(path):
    print(f"running {path}")
    df = pd.read_parquet(path)
    Y = df[DATES].iloc[:,7:7*60].fillna(0).values.astype(sp.float32).T
    print(Y.shape)
    lags = list(itertools.chain(
        range(1, 8), range(7 * 4, 8 * 4), range(7 * 8, 8 * 8)
    ))
    lag_set = sp.array(list(lags), dtype=sp.uint32)
    k = 40
    lambdaI = 2
    lambdaAR = 625
    lambdaLag = 0.5
    window_size = 7
    nr_windows = 1
    max_iter = 40
    threshold = 0
    threads = 40
    seed = 0
    missing = False
    transform = True
    threshold = None

    metrics = trmf.rolling_validate(
        Y,
        lag_set,
        k,
        window_size,
        nr_windows,
        lambdaI,
        lambdaAR,
        lambdaLag,
        max_iter=max_iter,
        threshold=threshold,
        transform=transform,
        threads=threads,
        seed=seed,
        missing=missing,
    )
    return metrics

if __name__ == "__main__":
    results = []
    for i in range(1, 11):
        path = f"data/design_matrix/sample_{i}_8_50"
        metrics = run_trial(path)
        # results.append(metrics)
        results.append({"mape": metrics.my_mape, "nrmse": metrics.my_rmse})
    df = pd.DataFrame(results)
    print(df)
    df.to_csv("trmf_trials.csv")