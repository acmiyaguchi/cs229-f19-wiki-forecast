import os
import string
from itertools import combinations
from time import time

import click
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from graphframes import GraphFrame


@click.command()
@click.option(
    "--pages-path",
    type=click.Path(exists=True, file_okay=False),
    default="data/enwiki/pages",
    help="Directory to page information parquet dataset.",
)
@click.option(
    "--pagelinks-path",
    type=click.Path(exists=True, file_okay=False),
    default="data/enwiki/pagelinks",
    help="Directory for page information ",
)
@click.option(
    "--pageviews-path",
    type=click.Path(exists=True, file_okay=False),
    default="data/enwiki/pagecount_daily_v2",
)
@click.option("--artifact-path", type=click.Path(file_okay=False), required=True)
@click.option("--article-seed", type=int, default=None, help="Center the sub-graph.")
@click.option("--k-hops", type=int, default=2, help="Radius of the sub-graph.")
# TODO: options for sub-sampling to mitigate skewed distributions
@click.option("--pagerank-alpha", type=float, default=0.85)
@click.option("--pagerank-tol", type=float, default=0.01)
def sample_subgraph(
    pages_path,
    pagelinks_path,
    pageviews_path,
    artifact_path,
    article_seed,
    k_hops,
    pagerank_alpha,
    pagerank_tol,
):
    start_time = time()
    click.echo("Starting!")

    if not os.path.exists(artifact_path):
        os.makedirs(artifact_path)

    # fetch the source datasets
    spark = SparkSession.builder.getOrCreate()
    pages = spark.read.parquet(pages_path)
    pagelinks = spark.read.parquet(pagelinks_path)
    pageviews = spark.read.parquet(pageviews_path)

    # extract induced subgraph
    graph = GraphFrame(pages, pagelinks.selectExpr("from as src", "dest as dst"))
    if not article_seed:
        article_seed = (
            graph.vertices.sample(False, 0.001).orderBy(F.rand()).limit(1).collect()[0]
        )
    induced_subgraph = sample_induced_subgraph(
        graph, article_seed.id, k_hops, pagerank_alpha, pagerank_tol
    )

    # write to disk
    with open(f"{artifact_path}/seed.txt", "w") as f:
        f.write(f"{article_seed.id},{article_seed.title}")

    edges_df = induced_subgraph.edges.toPandas()
    edges_df.to_csv(f"{artifact_path}/edges.csv", index=False)

    vertices_df = induced_subgraph.vertices.orderBy(F.desc("pagerank")).toPandas()
    vertices_df.to_csv(f"{artifact_path}/mapping.csv", index=False)
    end_time = time()
    click.echo(f"Done! Took {end_time-start_time}")


def sample_induced_subgraph(
    graph: GraphFrame,
    seed: int,
    k_hops: int = 2,
    pr_alpha: float = 0.85,
    pr_tol: float = 0.001,
) -> GraphFrame:
    assert k_hops <= 3

    # build motif for finding a k-hop neighborhood localized to a node
    symbols = string.ascii_letters
    motif_edges = [(symbols[i], symbols[i + 1]) for i in range(k_hops)]
    paths = graph.find(";".join([f"({e1})-[]->({e2})" for e1, e2 in motif_edges]))
    centered_paths = paths.where(f"{symbols[k_hops//2]}.id = {seed}")

    vertices = centered_paths.selectExpr(f"{symbols[0]} as v")
    for i in range(1, k_hops + 1):
        vertices = vertices.union(centered_paths.selectExpr(f"{symbols[i]} as v"))
    vertices = vertices.select("v.*").distinct()
    vertices.cache()

    edges = (
        graph.edges.join(vertices, on=graph.edges["src"] == vertices["id"], how="right")
        .select("src", "dst")
        .join(vertices, on=graph.edges["dst"] == vertices["id"], how="right")
        .select("src", "dst")
        .where("src is not null AND dst is not null")
    )
    return GraphFrame(vertices, edges).pageRank(pr_alpha, tol=pr_tol)
