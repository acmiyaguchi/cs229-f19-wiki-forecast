import click
import networkx as nx
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor

from .baseline import run_ablation, summarize
from .data import create_dataset, laplacian_embedding


def run_trial(mapping, edges, ts):
    embedding_size = 16
    window_size = 7
    num_windows = 54

    train, validate, test = create_dataset(ts, window_size, num_windows)
    print(f"train shape: {train.shape}")
    print(f"validate shape: {validate.shape}")
    print(f"test shape: {test.shape}")

    g = nx.subgraph(
        nx.from_pandas_edgelist(
            edges, source="src", target="dst", create_using=nx.Graph
        ),
        ts.id,
    )
    print(nx.info(g))
    emb = laplacian_embedding(g, embedding_size)
    pagerank = np.array([ts.merge(mapping).pagerank.values]).T
    print("MAPE\tRMSE\tmodel name")
    summarize("persistence", test, validate)
    summarize("mean", test, (np.ones(test.shape).T * validate.mean(axis=1)).T)

    model = MLPRegressor(solver="lbfgs")
    param_grid = dict(hidden_layer_sizes=[(3,), (3, 3), (4,), (4, 4)])
    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring="neg_mean_absolute_error",
        n_jobs=-1,
    )
    run_ablation("neural network (mae)", grid, train, validate, test, pagerank, emb)

    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring="neg_mean_squared_error",
        n_jobs=-1,
    )
    run_ablation("neural network (mse)", grid, train, validate, test, pagerank, emb)

    # TODO: min-max scaling + normalization
    # TODO: denoise time series using truncated-SVD
    # TODO: short-time fourier transform features (scipy.signal.stft)
    # TODO: wavlet transform features (scipy.wavelet.cwt)


@click.command()
@click.option("--mapping-path", default="sample_data/trial_6/mapping.csv")
@click.option("--edges-path", default="sample_data/trial_6/edges.csv")
@click.option("--ts-path", default="sample_data/trial_6/ts.csv")
def main(mapping_path, edges_path, ts_path):
    """Run experiments on a sampled graph that fits into memory"""
    mapping = pd.read_csv(mapping_path)
    edges = pd.read_csv(edges_path)
    ts = pd.read_csv(ts_path)
    run_trial(mapping, edges, ts)


if __name__ == "__main__":
    main()
