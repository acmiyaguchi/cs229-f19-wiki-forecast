import click
import time
import pandas as pd
import networkx as nx
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from .experiment_embedding import run_trial
from .baseline_random import sample_random, create_dataset_from_parquet


@click.command()
@click.option("--pages-path", default="data/enwiki/pages")
@click.option("--pagelinks-path", default="data/enwiki/pagelinks")
@click.option("--pageviews-path", default="data/enwiki/pagecount_daily_v2")
@click.option("--num-trials", default=1)
@click.option("--output-summary-file", default="embedding_random_summary_results.csv")
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
