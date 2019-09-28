import io

import click
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


@click.command()
@click.option("--artifact-path", type=click.Path(file_okay=False), required=True)
@click.option("--edges", type=str, default="edges.csv")
def summarize_graph(artifact_path, edges):
    graph = nx.from_pandas_edgelist(
        pd.read_csv(f"{artifact_path}/{edges}"), source="src", target="dst"
    )
    graph_statistics(graph, artifact_path)


@click.command()
@click.option("--artifact-path", type=click.Path(file_okay=False), required=True)
@click.option("--mapping-basename", type=str, default="mapping.csv")
@click.option("--pageview-basename", type=str, default="ts.csv")
@click.option(
    "--k-articles", type=int, default=10, help="Number of articles to include"
)
def summarize_pageview(artifact_path, mapping_basename, pageview_basename, k_articles):
    mapping = pd.read_csv(f"{artifact_path}/{mapping_basename}")
    pageview = pd.read_csv(f"{artifact_path}/{pageview_basename}")
    df = pd.merge(mapping[["id", "pagerank", "title"]], pageview, on="id")

    k = k_articles
    dates = pd.to_datetime(df.columns[3:])
    labels = df.title[:k].values
    X = df.iloc[:k, 3:].fillna(0).values.T

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(dates, X)
    ax.legend(labels)
    plt.yscale("log")
    fig.autofmt_xdate()
    plt.savefig(f"{artifact_path}/top_pagview.png")


def graph_statistics(g: nx.Graph, artifact_path: str):
    clustering_coeff = nx.average_clustering(g)
    density = nx.density(g)

    summary = io.StringIO()
    summary.write(f"{nx.info(g)}\n")
    summary.write(f"Clustering Coefficient: {clustering_coeff}\n")
    summary.write(f"Density: {density}\n")

    with open(f"{artifact_path}/summary.txt", "w") as f:
        f.write(summary.getvalue())
    print(summary.getvalue())

    plt.clf()
    nx.draw(g)
    plt.savefig(f"{artifact_path}/force_directed.png")

    plt.clf()
    nx.draw_spectral(g)
    plt.savefig(f"{artifact_path}/spectral.png")

    plt.clf()
    buckets = nx.degree_histogram(g)
    degrees = list(range(len(buckets)))
    plt.loglog(degrees, buckets)
    plt.savefig(f"{artifact_path}/degree_histogram.png")
