from typing import List
from pathlib import Path

import click
import numpy as np
import pandas as pd
import pyspark.sql.functions as F
import scipy.sparse as sp
from graphframes import GraphFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import PandasUDFType, pandas_udf
from scipy.sparse.csgraph import laplacian
from scipy.sparse.linalg import eigsh


def sparse_matrix_from_edgelist(edges):
    n = edges["src"].max()
    ones = np.ones(len(edges["dst"]))
    return sp.coo_matrix(
        (ones, (edges["src"], edges["dst"])), shape=(n + 1, n + 1)
    ).tocsr()


def fiedler_vector(g):
    L = laplacian(g)
    # ordered by smallest eigenvalue
    _, v = eigsh(L, k=2)
    # fiedler vector is the second smallest eigenvalue
    return v[:, 1]


@pandas_udf("id long, value double", PandasUDFType.GROUPED_MAP)
def compute_fiedler(pdf):
    g = sparse_matrix_from_edgelist(pdf)
    vec = fiedler_vector(g)
    return pd.DataFrame([{"id": i, "value": v} for i, v in enumerate(vec)])


def induce_graph(graph, relabel=True):
    """Remove extra edges that do not belong to the graph"""
    # small dataframe for reindexing/relabeling
    # O(50mb)
    rank = (
        graph.vertices.select(
            "id", F.expr("row_number() over (order by id)").alias("rank")
        )
        # ensure 0 index for mapping into a scipy.sparse matrix
        .withColumn("rank", F.expr("rank - 1"))
    )
    vertices = graph.vertices.join(F.broadcast(rank), on="id", how="inner")
    vertices.cache()
    edges = graph.edges.join(
        vertices.selectExpr("id as src", "rank as relabeled_src"), on="src", how="inner"
    ).join(
        vertices.selectExpr("id as dst", "rank as relabeled_dst"), on="dst", how="inner"
    )

    if relabel:
        vertices = vertices.withColumn("original_id", F.col("id")).withColumn(
            "id", F.col("rank")
        )
        edges = edges.selectExpr("relabeled_src as src", "relabeled_dst as dst")
    vertices = vertices.drop("rank")
    edges = edges.drop("relabeled_src").drop("relabeled_dst")
    vertices.unpersist()

    return GraphFrame(vertices, edges)


def sample_graph(pages, pagelinks, sampling_ratio, relabel=True):
    vertices = pages.sample(sampling_ratio)
    edges = pagelinks.selectExpr("from as src", "dest as dst")
    graph = induce_graph(GraphFrame(vertices, edges), False)
    # only do this when sampling, on the full dataset this is a waste of time
    components = graph.connectedComponents()
    components.cache()
    largest_component = (
        components.groupBy("component")
        .count()
        .orderBy(F.desc("count"))
        .limit(1)
        .select("component")
    )
    return induce_graph(
        GraphFrame(
            components.join(largest_component, on="component", how="inner"), graph.edges
        )
    )


def recursive_bipartition(graph: GraphFrame, max_iter: int = 2) -> GraphFrame:
    """
    Assumes the input graph has been relabeled, which is required for performance of
    scipy.linalg.eigsh.
    """

    def undo_relabel(vertices):
        return vertices.withColumn("id", F.col("original_id")).drop("original_id")

    def bipartition(graph: GraphFrame, partitions: List[str] = [], iteration: int = 0):

        partition = f"sign_{iteration}"
        fiedler_value = f"fiedler_{iteration}"
        fiedler = (
            graph.edges
            # necessary for collecting all edges to a single worker
            .withColumn("part", F.lit(True))
            .groupBy("part")
            .apply(compute_fiedler)
            .withColumn(partition, F.expr("value >= 0").astype("boolean"))
            .selectExpr("id", f"value as {fiedler_value}", partition)
        )

        # NOTE: assumes relabeling, reverse the relabeling process
        vertices = graph.vertices.join(fiedler, on="id", how="left")
        parted_graph = GraphFrame(vertices, graph.edges)
        parted_graph.cache()

        if iteration == max_iter:
            return undo_relabel(parted_graph.vertices)
        else:
            positive_vertices = bipartition(
                induce_graph(
                    GraphFrame(
                        parted_graph.vertices.where(f"{partition}"), parted_graph.edges
                    ),
                    relabel=True,
                ),
                partitions + [partition],
                iteration + 1,
            )
            negative_vertices = bipartition(
                induce_graph(
                    GraphFrame(
                        parted_graph.vertices.where(f"NOT {partition}"),
                        parted_graph.edges,
                    ),
                    relabel=True,
                ),
                partitions + [partition],
                iteration + 1,
            )
            # reusing the index, should this be saved?
            return undo_relabel(
                positive_vertices.union(negative_vertices).join(
                    parted_graph.vertices.select("id", "original_id"),
                    on="id",
                    how="inner",
                )
            )

    return bipartition(induce_graph(graph, relabel=True))


@click.command()
@click.option("--sample-ratio", type=float, default=0.05)
@click.option("--max-iter", type=int, default=2)
@click.option("--pages-path", default="data/enwiki/pages")
@click.option("--pagelinks-path", default="data/enwiki/pagelinks")
@click.option("--output-path", type=str, required=True)
@click.option(
    "--checkpoint-dir",
    default="file:///" + "/".join((Path(".").resolve() / "data/tmp").parts[1:]),
)
def main(
    sample_ratio, max_iter, pages_path, output_path, pagelinks_path, checkpoint_dir
):
    spark = SparkSession.builder.appName("recursive bipartitioning").getOrCreate()
    spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    spark.conf.set("spark.sql.shuffle.partitions", "16")
    spark.conf.set("spark.sql.execution.arrow.enabled", "true")
    spark.sc.setCheckpointDir(checkpoint_dir)

    pages = spark.read.parquet(pages_path)
    pagelinks = spark.read.parquet(pagelinks_path)

    g = sample_graph(pages, pagelinks, sample_ratio)
    g.cache()

    parted = recursive_bipartition(g, max_iter=2)
    parted.repartition(4).save.parquet(output, mode="overwrite")
