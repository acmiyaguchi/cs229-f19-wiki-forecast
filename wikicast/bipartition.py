from typing import List
from pathlib import Path
from time import time

import click
import numpy as np
import pandas as pd
import scipy.sparse as sp
from graphframes import GraphFrame
from pyspark.sql import SparkSession, Window, functions as F
from pyspark.sql.functions import PandasUDFType, pandas_udf
from scipy.sparse.csgraph import laplacian
from scipy.sparse.linalg import eigsh


def sparse_matrix_from_edgelist(edges):
    n = max(edges["src"].max(), edges["dst"].max())
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


def induce_graph(graph, relabel=True, partitions=[]):
    """Remove extra edges that do not belong to the graph"""
    # small dataframe for reindexing/relabeling
    # O(50mb)

    window = Window.orderBy("id")
    if partitions:
        window = window.partitionBy(partitions)

    # ensure 0 index for mapping into a scipy.sparse matrix
    rank = graph.vertices.select(
        "id", F.row_number().over(window).alias("rank")
    ).withColumn("rank", F.expr("rank - 1"))

    vertices = graph.vertices.join(rank, on="id", how="inner")
    vertices.cache()

    edges = graph.edges.join(
        vertices.selectExpr("id as src"), on="src", how="inner"
    ).join(vertices.selectExpr("id as dst"), on="dst", how="inner")

    if relabel:
        vertices = vertices.withColumn("relabeled_id", F.col("id")).withColumn(
            "id", F.col("rank")
        )

    vertices = vertices.drop("rank")
    vertices.unpersist()
    return GraphFrame(vertices, edges)


def undo_relabel(vertices, name="id", prefix="relabeled"):
    return vertices.withColumn(name, F.col(f"{prefix}_{name}")).drop(f"{prefix}_{name}")


def recursive_bipartition(graph: GraphFrame, max_iter: int = 2) -> GraphFrame:
    """
    Assumes the input graph has been relabeled, which is required for performance of
    scipy.linalg.eigsh.
    """

    @pandas_udf("id long, value double", PandasUDFType.GROUPED_MAP)
    def compute_fiedler(key, pdf):
        print(key)
        if any(k == None for k in key):
            print("disconnected edges for this iteration")
            return pd.DataFrame([{"id": -1, "value": None}])
        g = sparse_matrix_from_edgelist(pdf)
        vec = fiedler_vector(g)
        return pd.DataFrame([{"id": i, "value": v} for i, v in enumerate(vec)])

    def bipartition(graph: GraphFrame, partitions: List[str] = [], iteration: int = 0):

        partition = f"sign_{iteration}"
        fiedler_value = f"fiedler_{iteration}"

        if iteration == max_iter:
            return graph

        # relabel all partitions and compute the fiedler vector for each one
        induced = induce_graph(graph, True, partitions)
        induced.edges.cache()
        induced.edges.checkpoint()

        fiedler = (
            induced.edges.groupBy(*partitions)
            .apply(compute_fiedler)
            .withColumn(partition, F.expr("value >= 0").astype("boolean"))
            .selectExpr("id", f"value as {fiedler_value}", partition)
        )

        vertices = induced.vertices.join(fiedler, on="id", how="leftouter")
        vertices.cache()
        vertices.checkpoint()

        # reverse the relabeling process and add the new partition to edge
        # attributes
        edges = (
            undo_relabel(
                undo_relabel(
                    induced.edges.join(
                        vertices.selectExpr(
                            "id as src",
                            "relabeled_id as relabeled_src",
                            f"{partition} as {partition}_left",
                            *partitions,
                        ),
                        on=["src"] + partitions,
                        how="leftouter",
                    ),
                    name="src",
                ).join(
                    vertices.selectExpr(
                        "id as dst",
                        "relabeled_id as relabeled_dst",
                        f"{partition} as {partition}_right",
                        *partitions,
                    ),
                    on=["dst"] + partitions,
                    how="leftouter",
                ),
                name="dst",
            )
            .withColumn(
                partition,
                F.when(
                    F.expr(f"{partition}_left = {partition}_right"),
                    F.col(f"{partition}_left"),
                ).otherwise(F.lit(None)),
            )
            .drop(f"{partition}_left")
            .drop(f"{partition}_right")
        )

        parted_graph = GraphFrame(undo_relabel(vertices), edges)
        return bipartition(parted_graph, partitions + [partition], iteration + 1)

    bias = "bias"
    vertices = graph.vertices.withColumn(bias, F.lit(True))
    edges = graph.edges.withColumn(bias, F.lit(True))
    return bipartition(GraphFrame(vertices, edges), [bias], 0)


def sample_graph(pages, pagelinks, sampling_ratio, relabel=True, ensure_connected=True):
    vertices = pages.sample(sampling_ratio)
    edges = pagelinks.selectExpr("from as src", "dest as dst")
    graph = induce_graph(GraphFrame(vertices, edges), False)
    if ensure_connected:
        # only do this when sampling, on the full dataset takes 12 minutes. This may
        # be required in order to guarantee connectivity.
        components = graph.connectedComponents()
        components.cache()
        largest_component = (
            components.groupBy("component")
            .count()
            .orderBy(F.desc("count"))
            .limit(1)
            .select("component")
        )
        vertices = components.join(largest_component, on="component", how="inner").drop(
            "component"
        )
        components.unpersist()
        return induce_graph(GraphFrame(vertices, graph.edges))
    else:
        return graph


@click.command()
@click.option("--sample-ratio", type=float, default=0.05)
@click.option("--max-iter", type=int, default=2)
@click.option("--pages-path", default="data/enwiki/pages")
@click.option("--pagelinks-path", default="data/enwiki/pagelinks")
@click.option("--output-path", type=str, required=True)
@click.option("--skip-connectivity-check/--no-skip-connectivity-check", default=False)
@click.option(
    "--checkpoint-dir",
    default="file:///" + "/".join((Path(".").resolve() / "data/tmp").parts[1:]),
)
def main(
    sample_ratio,
    max_iter,
    pages_path,
    output_path,
    pagelinks_path,
    checkpoint_dir,
    skip_connectivity_check,
):
    spark = SparkSession.builder.appName("recursive bipartitioning").getOrCreate()
    spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    spark.conf.set("spark.sql.execution.arrow.enabled", "true")
    spark.sparkContext.setCheckpointDir(checkpoint_dir)

    pages = spark.read.parquet(pages_path)
    pagelinks = spark.read.parquet(pagelinks_path)

    graph = sample_graph(
        pages, pagelinks, sample_ratio, ensure_connected=not skip_connectivity_check
    )
    graph.cache()
    sample_vertices_count = graph.vertices.count()
    sample_edges_count = graph.edges.count()

    parted = recursive_bipartition(graph, max_iter)
    parted.vertices.cache()
    start = time()
    parted.vertices.repartition(4).write.parquet(
        f"{output_path}/vertices", mode="overwrite"
    )
    parted.edges.repartition(4).write.parquet(f"{output_path}/edges", mode="overwrite")
    print(f"clustering took {time()-start} seconds")

    parted.vertices.printSchema()
    parted.edges.printSchema()

    parted.vertices.groupBy(
        *(["bias"] + [c for c in parted.vertices.columns if c.startswith("sign_")])
    ).count().orderBy(F.desc("count")).show()
    print(
        f"partitioned graph has {parted.vertices.count()} vertices and {parted.edges.count()} edges"
    )
    print(
        f"sampled graph has {sample_vertices_count} vertices and {sample_edges_count} edges"
    )
