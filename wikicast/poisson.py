import numpy as np
import matplotlib.pyplot as plt
import os
import click

import util


class PoissonRegression:
    """Poisson Regression.

    Example usage:
        > clf = PoissonRegression(step_size=lr)
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def __init__(
        self, step_size=1e-5, max_iter=10000000, eps=1e-5, theta_0=None, verbose=False
    ):
        """
        Args:
            step_size: Step size for iterative solvers only.
            max_iter: Maximum number of iterations for the solver.
            eps: Threshold for determining convergence.
            theta_0: Initial guess for theta. If None, use the zero vector.
            verbose: Print loss values during training.
        """
        self.theta = theta_0
        self.step_size = step_size
        self.max_iter = max_iter
        self.eps = eps
        self.verbose = verbose

    def fit(self, x, y):
        """Run gradient ascent to maximize likelihood for Poisson regression.

        Args:
            x: Training example inputs. Shape (n_examples, dim).
            y: Training example labels. Shape (n_examples,).
        """
        # *** START CODE HERE ***
        n_examples = x.shape[0]
        d = x.shape[1]
        print(f"n_examples:{n_examples} d:{d}")

        self.theta = np.zeros(d)

        previous_delta_norm = 10000 * self.eps
        delta_norm = 1000 * self.eps
        iter = 0  

        y_1 = y.reshape((n_examples, 1))
        step_size = self.step_size
        while iter < self.max_iter and delta_norm > self.eps:
            z = np.exp(np.dot(x, self.theta)).reshape((n_examples, 1))
            update = np.zeros(5)
            update = np.sum((y_1 - z) * x, axis=0)
            previous_delta_norm = delta_norm
            delta_norm = np.linalg.norm(self.step_size * update, ord=1)
            self.theta = self.theta + self.step_size * update
            iter += 1
            if iter % 250 == 0:
                print('theta=', self.theta, 'delta=', delta_norm, 'iter=', iter)
        print('theta=', self.theta)
    def predict(self, x):
        """Make a prediction given inputs x.

        Args:
            x: Inputs of shape (n_examples, dim).

        Returns:
            Floating-point prediction for each input, shape (n_examples,).
        """
        predict = np.exp(np.dot(x, self.theta))
        return predict


def plot(eval, predict):
    plt.scatter(y_eval, y_predict)
    plt.axis(xmin=0, xmax=30, ymin=0, ymax=30)
    plt.xlim(-2, y_eval.max() + 2)
    plt.ylim(0, y_predict.max() + 2)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")


def main(train, eval, learning_rate, train_path, save_path=None):
    """Evaluate Poisson regression with gradient ascent with matrix solutions.

    Args:
        train:
        eval:
        learning_rate:
        save_path:
    """
    # train, validate, test = util.load_dataset(train_path, add_intercept=True)

    poisson_reg = PoissonRegression()
    poisson_reg.fit(x_train, y_train)

    x_eval, y_eval = util.load_dataset(eval_path, add_intercept=True)
    y_predict = poisson_reg.predict(x_eval)

    np.savetxt(save_path, y_predict)
    plot(eval, predict)


if __name__ == "__main__":
    main(
        lr=1e-5,
        train_path="train.csv",
        eval_path="valid.csv",
        save_path="poisson_pred.txt",
    )
