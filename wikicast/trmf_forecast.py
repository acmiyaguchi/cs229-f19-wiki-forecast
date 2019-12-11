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

if __name__ == "__main__":
    df = pd.read_parquet("data/design_matrix/sample_10_8_50")
    Y = df[DATES].iloc[:50000,7:7*60].fillna(0).values.astype(sp.float32).T
    print(Y.shape)
    lags = list(itertools.chain(
        range(1, 8), range(7 * 4, 8 * 4), range(7 * 8, 8 * 8)
    ))
    print(list(lags))
    #lags = list(range(1, 8))
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
    print(metrics)
