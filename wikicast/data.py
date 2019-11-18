import numpy as np
import matplotlib.pyplot as plt


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


# TODO
# def load_dataset(path, add_intercept: bool = False):
#   pass
