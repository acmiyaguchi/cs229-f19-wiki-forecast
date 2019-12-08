import numpy as np
import matplotlib.pyplot as plt
import os
import click
import statsmodels.api as sm

from . import data


class PoissonRegression:
    def __init__(self):
        self.model = []
        self.fitted = []

    def fit(self, x, y):
        if len(y.shape) == 1:
            y = y.reshape(-1, 1)
        self.model = []
        for j in range(y.shape[1]):
            model = sm.GLM(
                endog=y[:, j], exog=x, family=sm.families.Poisson(), link="log"
            )
            self.fitted.append(model.fit())
            self.model.append(model)

    def predict(self, x):
        results = []
        for model, fitted in zip(self.model, self.fitted):
            results.append(model.predict(fitted.params, x))
        return np.array(results).T


@click.command()
@click.option("--learning-rate", default=1e-5)
@click.option("--train-path", help="e.g. train.csv")
@click.option("--eval-path", help="e.g. valid.csv")
@click.option("--save-path", help="e.g. poisson_pred.txt")
def main(learning_rate, train_path, eval_path, save_path):
    """Evaluate Poisson regression with gradient ascent with matrix solutions.
    """
    # TODO: train, validate, test = util.load_dataset(train_path, add_intercept=True)
    train, validate, test = data.generate_poisson(
        n_series=10 ** 4, t_values=14 * 7, window_size=7, lambda_param=3
    )

    poisson_reg = PoissonRegression()
    poisson_reg.fit(train, validate)

    y_predict = poisson_reg.predict(validate)
    if save_path:
        np.savetxt(save_path, y_predict)


if __name__ == "__main__":
    main()
