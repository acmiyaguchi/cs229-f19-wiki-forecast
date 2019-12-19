import click
import time
import pandas as pd
import networkx as nx
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from .baseline import run_trial


def sample_random(pages, links, views):
    # TODO: expose this argument, add deterministic seed
    sampling_ratio = 0.05

    nodes = pages.sample(sampling_ratio)
    edges = (
        links.join(nodes.selectExpr("id as from"), on="from").join(
            nodes.selectExpr("id as dest"), on="dest"
        )
    ).selectExpr("from as src", "dest as dst")
    ts = (
        views.join(nodes, on=views["page_id"] == nodes["id"])
        .where("date is not null")
        .groupBy("id")
        .pivot("date")
        .agg(F.min("count"))
    )
    return nodes.toPandas(), edges.toPandas(), ts.toPandas()


def create_dataset_from_parquet(pages, links, views):
    mapping, edges, ts = sample_random(pages, links, views)

    # get subgraph and compute pagerank
    g = nx.subgraph(
        nx.from_pandas_edgelist(
            edges, source="src", target="dst", create_using=nx.DiGraph
        ),
        ts.id,
    )
    print(f"sampled graph has {g.number_of_nodes()} nodes")
    pr = nx.pagerank(g)
    ordered = sorted(pr.keys(), key=pr.get, reverse=True)

    # only keep the largest connected component, top pagerank node is most
    # likely to be part of the largest fully connected component
    g = nx.Graph(g).subgraph(nx.node_connected_component(nx.Graph(g), ordered[0]))
    print(f"largest component has {g.number_of_nodes()} nodes")

    # create a list sorted by pagerank
    connected = pd.DataFrame(
        {"id": g.nodes(), "pagerank": [pr[x] for x in g.nodes()]}
    ).sort_values("pagerank", ascending=False)
    return connected.merge(mapping), edges, connected.merge(ts).drop("pagerank", axis=1)


@click.command()
@click.option("--pages-path", default="data/enwiki/pages")
@click.option("--pagelinks-path", default="data/enwiki/pagelinks")
@click.option("--pageviews-path", default="data/enwiki/pagecount_daily_v2")
@click.option("--num-trials", default=1)
@click.option("--output-summary-file", default="summary_results.csv")
def main(pages_path, pagelinks_path, pageviews_path, num_trials, output_summary_file):
    pd.set_option("display.max_colwidth", -1)

    spark = SparkSession.builder.getOrCreate()

    pages = spark.read.parquet(pages_path)
    pagelinks = spark.read.parquet(pagelinks_path)
    pageviews = spark.read.parquet(pageviews_path)

    results = []
    for trial_id in range(num_trials):
        start = time.time()
        mapping, edges, ts = create_dataset_from_parquet(pages, pagelinks, pageviews)
        print(f"sampling took {time.time() - start} seconds")
        results += run_trial(mapping, edges, ts, trial_id=trial_id)

    df = pd.DataFrame(results)[["name", "mape", "rmse", "trial_id"]]
    print(df)
    df.to_csv(output_summary_file)


@click.command()
@click.option("--pages-path", default="data/enwiki/pages")
@click.option("--pagelinks-path", default="data/enwiki/pagelinks")
@click.option("--pageviews-path", default="data/enwiki/pagecount_daily_v2")
@click.option("--output", default="data/results/sampled_1")
def write_sample(pages_path, pagelinks_path, pageviews_path, output):

    spark = SparkSession.builder.getOrCreate()

    pages = spark.read.parquet(pages_path)
    pagelinks = spark.read.parquet(pagelinks_path)
    pageviews = spark.read.parquet(pageviews_path)
    mapping, edges, ts = create_dataset_from_parquet(pages, pagelinks, pageviews)
    mapping.to_csv(f"{output}/mapping.csv")
    edges.to_csv(f"{output}/edges.csv")
    ts.to_csv(f"{output}/ts.csv")

if __name__ == "__main__":
    write_sample()