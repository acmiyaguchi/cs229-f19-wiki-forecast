import numpy as np
import matplotlib.pyplot as plt
import os
import click

from . import data


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
            y: Training example labels. Shape (n_examples, output_dim), or
                (n_examples,) if output_dim = 1.
        """
        # *** START CODE HERE ***
        n_examples = x.shape[0]
        d = x.shape[1]
        print(f"n_examples:{n_examples} d:{d}")
        if len(y.shape) == 1:
          output_dim = 1
        else:
          output_dim = y.shape[1]
          

        self.theta = np.zeros((output_dim, d))

        for k in range(output_dim):
          if output_dim == 1: 
            y_1 = y.reshape((n_examples, 1))
          else:
            y_1 = y[:,k].reshape((n_examples, 1))
          previous_delta_norm = 10000 * self.eps
          delta_norm = 1000 * self.eps
          iter = 0

          step_size = self.step_size
          while iter < self.max_iter and (np.abs(delta_norm - previous_delta_norm)/previous_delta_norm) > self.eps:
              z = np.exp(np.matmul(x, self.theta[k].T)).reshape((n_examples, 1))
              update = np.sum((y_1 - z) * x, axis=0)
              previous_delta_norm = delta_norm
              delta_norm = np.linalg.norm(self.step_size * update, ord=1)
              self.theta[k] = self.theta[k] + self.step_size * update
              iter += 1
              if iter % 250 == 0:
                  pass
                  # print("theta=", self.theta[k], "delta=", delta_norm, "iter=", iter)
          # print("theta=", self.theta)

    def predict(self, x):
        """Make a prediction given inputs x.

        Args:
            x: Inputs of shape (n_examples, dim).

        Returns:
            Floating-point prediction for each input, shape (n_examples, output_dim).
        """
        predict = np.exp(np.matmul(x, self.theta.T))
        return predict


def plot(eval, predict):
    # TODO: fix this for the multi-dim case.
    plt.scatter(y_eval, y_predict)
    plt.axis(xmin=0, xmax=30, ymin=0, ymax=30)
    plt.xlim(-2, y_eval.max() + 2)
    plt.ylim(0, y_predict.max() + 2)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")


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
