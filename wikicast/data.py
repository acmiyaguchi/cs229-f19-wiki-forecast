import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import scipy.sparse as ss
from pyspark.ml.linalg import Vectors, VectorUDT
from pyspark.sql.functions import udf, col


def rmse(y, y_pred):
    return np.sqrt(np.sum((y - y_pred) ** 2) / y.size)


def mape(y, y_pred):
    return np.sum(abs(np.divide(y - y_pred, y))) / y.size * 100


def rmse_df(df, y="label", y_pred="prediction"):
    return (
        df.selectExpr(
            f"sqrt(sum(pow({y} - {y_pred}, 2)))/count(distinct page_id)) as rmse"
        )
        .first()
        .rmse
    )
    return np.sqrt(np.sum((y - y_pred) ** 2) / y.size)


def mape_df(df, y="label", y_pred="prediction"):
    return df.selectExpr(f"avg(abs({y} - {y_pred})/{y})*100 as mape").first().mape


def generate_poisson(n_series, t_values, window_size, lambda_param):
    Y = np.random.poisson(lambda_param, (n_series, t_values))
    t = lambda index: [np.newaxis, window_size, 2 * window_size, 3 * window_size][index]
    train, validate, test = Y[:, t(0) : t(1)], Y[:, t(1) : t(2)], Y[:, t(2) : t(3)]
    return train, validate, test


def laplacian_embedding(g, dim):
    L = nx.laplacian_matrix(g).astype("float64")
    w, v = ss.linalg.eigsh(L, k=dim + 1)
    return np.divide(v[:, :-1], np.sqrt(w[:-1]))[::-1]


def create_dataset(ts, window_size=7, n_panes=14, missing_value_default=1e-6,
                   normalize=False):
    # fill missing days with very small values
    X = ts.iloc[:, 1:].fillna(missing_value_default).values
    
    if normalize:
      X = (X - X.mean(axis=1).reshape(-1, 1)) / (X.max(axis=1) - X.min(axis=1)).reshape(-1, 1)   
    
    T = X.shape[1]
    window_size = 7

    # Create a new matrix for every row that is matrix of size (T//window_size, window_size)
    indexer = np.arange(window_size).reshape(1, -1) + window_size * np.arange(
        T // window_size
    ).reshape(-1, 1)

    # A pane is made up of many windows
    panes = X[:, indexer]

    # by default, concatenate 4*3 windows, or 3 months of data, for the training data
    train = panes[:, : n_panes - 2, :].reshape(panes.shape[0], -1)

    # we benchmark this against using the previous week's day
    validate = panes[:, n_panes - 1, :]

    # the test data is the final week
    test = panes[:, n_panes, :]

    return train, validate, test


@udf(VectorUDT())
def fill_nan(vec: np.array, num=0):
    return Vectors.dense(np.nan_to_num(vec, num))


@udf(VectorUDT())
def denoise(vec: np.array, window_size=7, scale=True):
    # Create a new matrix for every row that is matrix of size (T//window_size, window_size)
    T = vec.shape[0]
    indexer = np.arange(window_size).reshape(1, -1) + window_size * np.arange(
        T // window_size
    ).reshape(-1, 1)

    # A page is made up of many windows
    page = vec[indexer]
    imputed = np.nan_to_num(page)
    if scale:
        scaled = imputed - imputed.mean(axis=0)
    u, s, vh = np.linalg.svd(scaled, full_matrices=False)

    k = window_size - 1
    return Vectors.dense(u[:, :k].dot(np.diag(s[:k])).dot(vh[:k]).reshape(-1))


# TODO
# def load_dataset(path, add_intercept: bool = False):
#   pass
