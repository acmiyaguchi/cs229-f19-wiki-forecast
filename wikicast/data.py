import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import scipy.sparse as ss


def rmse(y, y_pred):
    return np.sqrt(np.sum(y - y_pred) ** 2)


def mape(y, y_pred):
    return np.sum(np.ma.divide(np.abs(y - y_pred), np.abs(y)).filled(0)) * 100


def summarize(validate, train, test):
    print("validate", rmse(validate, train), mape(validate, train))
    print("test", rmse(test, validate), mape(test, validate))


def generate_poisson(n_series, t_values, window_size, lambda_param):
    Y = np.random.poisson(lambda_param, (n_series, t_values))
    t = lambda index: [np.newaxis, window_size, window_size + 1, window_size + 2][index]
    train, validate, test = Y[:, t(0) : t(1)], Y[:, t(1) : t(2)].T, Y[:, t(2) : t(3)].T
    return train, validate, test


def laplacian_embedding(g, dim):
    L = nx.laplacian_matrix(g).astype("float64")
    w, v = ss.linalg.eigsh(L, k=dim + 1)
    return np.divide(v[:, :-1], np.sqrt(w[:-1]))[::-1]


def create_dataset(ts, window_size=7, n_panes=14):
    # fill missing days with very small values
    X = ts.iloc[:, 1:].fillna(1e-6).values
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


# TODO
# def load_dataset(path, add_intercept: bool = False):
#   pass
