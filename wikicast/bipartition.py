from typing import List
from pathlib import Path
from time import time
import functools

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

    window = Window.orderBy("id")
    if partitions:
        window = window.partitionBy(partitions)

    # ensure 0 index for mapping into a scipy.sparse matrix
    rank = graph.vertices.select(
        "id", F.row_number().over(window).alias("rank")
    ).withColumn("rank", F.expr("rank - 1"))

    vertices = graph.vertices.join(rank, on="id", how="left")

    edges = graph.edges.join(
        vertices.selectExpr("id as src", "rank as rank_src"), on="src", how="inner"
    ).join(vertices.selectExpr("id as dst", "rank as rank_dst"), on="dst", how="inner")

    if relabel:
        vertices = vertices.withColumn("relabeled_id", F.col("id")).withColumn(
            "id", F.col("rank")
        )
        edges = (
            edges.withColumn("relabeled_src", F.col("src"))
            .withColumn("relabeled_dst", F.col("dst"))
            .withColumn("src", F.col("rank_src"))
            .withColumn("dst", F.col("rank_dst"))
        )

    vertices = vertices.drop("rank")
    edges = edges.drop("rank_src", "rank_dst")
    return GraphFrame(vertices, edges)


def undo_relabel(vertices, name="id", prefix="relabeled"):
    return vertices.withColumn(name, F.col(f"{prefix}_{name}")).drop(f"{prefix}_{name}")


def edges_with_partitions(graph, partitions):
    """
    Assign each edge to a partition. If the edge is between two partitions, it
    is removed from the set. The select and where clauses are manually
    specificed because two sets of joins lead to ambiguity in the partition
    column. e.g.

        Resolved attribute(s) bias#530 missing from
        is_new#224,bias#208,is_redirect#223,id#221,title#222 in operator
        !Project [id#221, bias#530]
    """
    partitions_src = [F.expr(f"{c} as {c}_src") for c in partitions]
    partitions_dst = [F.expr(f"{c} as {c}_dst") for c in partitions]
    assign_edges = [
        F.when(F.expr(f"{c}_src = {c}_dst"), F.col(f"{c}_src"))
        .otherwise(F.lit(None))
        .alias(c)
        for c in partitions
    ]
    edges_filter = functools.reduce(
        lambda x, y: x & y, [F.col(c).isNotNull() for c in partitions]
    )

    edges = (
        graph.edges.join(
            graph.vertices.select(
                F.expr("relabeled_id as relabeled_src"), *partitions_src
            ),
            on="relabeled_src",
            how="left",
        )
        .join(
            graph.vertices.select(
                F.expr("relabeled_id as relabeled_dst"), *partitions_dst
            ),
            on="relabeled_dst",
            how="left",
        )
        .select("src", "dst", *assign_edges)
        .where(edges_filter)
        .repartitionByRange(*partitions)
    )
    return edges


def compute_fiedler_udf(fiedler_value, partitions):
    part_schema = ", ".join(f"{c} boolean" for c in partitions)

    @pandas_udf(
        f"{part_schema}, id long, {fiedler_value} double", PandasUDFType.GROUPED_MAP
    )
    def compute_fiedler(keys, pdf):
        # unfortunately, adding the extra join key columns is the only way
        # to map the values back to the nodes
        g = sparse_matrix_from_edgelist(pdf)
        vec = fiedler_vector(g)
        df = pd.DataFrame(vec, columns=[fiedler_value])
        df["id"] = np.arange(vec.size)
        for name, value in zip(partitions, list(keys)):
            df[name] = value
        return df

    return compute_fiedler


def recursive_bipartition(
    graph: GraphFrame, max_iter: int = 2, should_checkpoint=True, checkpoint_interval=2
) -> GraphFrame:
    def bipartition(graph: GraphFrame, partitions: List[str] = [], iteration: int = 0):

        if iteration == max_iter:
            return graph

        # relabel all partitions for scipy.sparse performance
        graph.cache()
        induced = induce_graph(graph, True, partitions)
        induced.cache()

        partition = f"sign_{iteration}"
        fiedler_value = f"fiedler_{iteration}"

        # The fiedler vector is the second smallest eigenvector associated with
        # with the graph laplacian, representing the algebraic connectivity of
        # the graph. This is used to implement spectral clustering, recursively,
        # by partitioning by the sign of the fiedler value. The partitions are
        # evenly distributed.
        fiedler = (
            edges_with_partitions(induced, partitions)
            .groupBy(*partitions)
            .apply(compute_fiedler_udf(fiedler_value, partitions))
            .withColumn(partition, F.expr(f"{fiedler_value} >= 0").astype("boolean"))
        )
        vertices = undo_relabel(
            induced.vertices.join(
                fiedler, on=["id"] + partitions, how="left"
            ).repartitionByRange(*partitions + [partition])
        )

        if should_checkpoint and iteration % checkpoint_interval == 0:
            # truncate logical plan to prevent out-of-memory on query plan
            # string representation. The edges are reused every iteration
            # and should not need to be checkpointed.
            vertices.cache()
            parted_graph = GraphFrame(vertices.localCheckpoint(eager=True), graph.edges)
        else:
            parted_graph = GraphFrame(vertices, graph.edges)

        return bipartition(parted_graph, partitions + [partition], iteration + 1)

    # initialize the recursive function
    bias = "bias"
    vertices = graph.vertices.withColumn(bias, F.lit(True))
    edges = graph.edges
    partitioned = bipartition(GraphFrame(vertices, edges), [bias], 0)
    return partitioned


def sample_graph(pages, pagelinks, sampling_ratio, relabel=True, ensure_connected=True):
    vertices = pages.sample(sampling_ratio)
    edges = pagelinks.selectExpr("from as src", "dest as dst")
    graph = induce_graph(GraphFrame(vertices, edges), False)
    if ensure_connected:
        # only do this when sampling, on the full dataset takes 12 minutes. This may
        # be required in order to guarantee connectivity.
        components = graph.connectedComponents()
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

    start = time()
    parted = recursive_bipartition(graph, max_iter)
    parted.vertices.repartition(4).write.parquet(output_path, mode="overwrite")
    total_time = time() - start

    vertices = spark.read.parquet(output_path)
    num_vertices = vertices.count()

    columns = ["bias"] + [c for c in vertices.columns if c.startswith("sign_")]
    vertices.groupBy(*columns).count().orderBy(*columns).show()
    print(f"clustering took {total_time} seconds")
    print(f"graph has {num_vertices} vertices")
    vertices.printSchema()

    spark.sparkContext.show_profiles()
