import csv
import sys

import click
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_hist(df):

    xlabels = df.index.values
    y = df[("rmse", "mean")]
    stdv = df[("rmse", "std")]

    ax = df.plot.bar(y=("rmse", "mean"))
    ax.errorbar(xlabels, df[("rmse", "mean")], yerr=df[("rmse", "std")], fmt="none")

    plt.show()


@click.command()
@click.option("--summary_data_file", default="summary_results.csv")
def main(summary_data_file):
    summary = pd.read_csv(summary_data_file)
    print(summary)
    print(summary.info())
    df = summary.groupby(["name"]).agg(
        {
            "rmse": ["min", "max", "mean", "std", "count"],
            "mape": ["min", "max", "mean", "std", "count"],
        }
    )
    print(df)
    plot_hist(df)


if __name__ == "__main__":
    main()
