import click
from pyspark.sql import SparkSession, functions as F
import pandas as pd


def extract(mapping, pageview):
    return (
        pageview.join(mapping, on=pageview["page_id"] == mapping["id"], how="right")
        .where("date is not null")
        .groupBy("id")
        .pivot("date")
        .agg(F.min("count"))
    )


@click.command()
@click.option(
    "--artifact-path", type=click.Path(exists=True, file_okay=False), required=True
)
@click.option(
    "--mapping-basename",
    type=str,
    default="mapping.csv",
    help="Dataset with id and titles",
)
@click.option(
    "--pageview-path",
    type=click.Path(exists=True, file_okay=False),
    default="data/enwiki/pagecount_daily_v2",
    help="Dataset with pagecount data at a daily granularity.",
)
def main(artifact_path, mapping_basename, pageview_path):
    spark = SparkSession.builder.getOrCreate()
    mapping = spark.read.csv(f"{artifact_path}/{mapping_basename}", header=True)
    pageview = spark.read.parquet(pageview_path)

    # order the time series by pagerank score
    ts = extract(mapping, pageview)
    df = mapping.select("id", "pagerank").join(ts, on="id").toPandas()
    df.sort_values(by=["pagerank"], ascending=False).drop(columns=["pagerank"]).to_csv(
        f"{artifact_path}/ts.csv", index=False
    )
