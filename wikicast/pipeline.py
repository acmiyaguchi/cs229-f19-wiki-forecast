"""
## Spark ML Pipeline for Wikipedia Traffic Forecasting
We construct the entire pipeline for learning a generalized linear model and a
neural network.
"""
from datetime import datetime, timedelta

import click
import numpy as np
from pyspark.ml import Pipeline
from pyspark.ml.feature import Imputer, SQLTransformer, StandardScaler, VectorAssembler
from pyspark.ml.regression import GeneralizedLinearRegression
from pyspark.sql import functions as F, SparkSession

from .data import denoise, rmse_df, mape_df


def extract(spark, pagecount: str, pages: str, pagelinks: str):
    pagecount = spark.read.parquet(pagecount)
    pages = spark.read.parquet(pages)
    pagelinks = spark.read.parquet(pagelinks)
    return pagecount, pages, pagelinks


def transform(pagecount):
    """Create a time-series vector for each page."""
    dataset = pagecount.groupBy("page_id").pivot("date").agg(F.min("count"))

    return dataset


def assembler(output_name, input_dates):
    return VectorAssembler(
        inputCols=input_dates, outputCol=output_name
    ).setHandleInvalid("keep")


def create_pipeline(train_dates, validate_dates, retrain_dates, test_dates):
    return Pipeline(
        stages=[
            assembler("train", train_dates),
            assembler("validate", validate_dates),
            assembler("retrain", retrain_dates),
            assembler("test", test_dates),
        ]
    )


def train_fit_glmm(window, date_label: str):
    poisson_regression = GeneralizedLinearRegression(
        family="poisson", link="log", maxIter=10, regParam=0.3
    )

    columns = [denoise("train").alias("features"), F.expr(f"{date_label} as label")]
    model = poisson_regression.fit(window.select(*columns))
    # TODO: may want to persist the fitted model
    observations = model.transform(window.withColumn("features", denoise("retrain")))

    columns = ["page_id", "train", "validate", "retrain", "test", "prediction"]
    return observations.select(*columns)


@click.command()
@click.option("--pagecount", default="data/enwiki/pagecount_daily_v2")
@click.option("--pages", default="data/enwiki/pages")
@click.option("--pagelinks", default="data/enwiki/pagelinks")
@click.option("--training-period", type=int, default=7 * 12)
@click.option("--period", type=int, default=7)
@click.option("--start-date", default="2019-01-01")
def main(pagecount, pages, pagelinks, training_period, period, start_date):
    spark = SparkSession.builder.getOrCreate()
    spark.conf.set("spark.sql.shuffle.partitions", 64)
    pagecount, pages, pagelinks = extract(spark, pagecount, pages, pagelinks)

    # We uses a list of datestrings to vectorize a group of columns. We define
    # the period which we will use for rolling evaluation of the model loss.
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    get_name = lambda t: (start_date + timedelta(t)).strftime("%Y-%m-%d")
    train_dates = [get_name(t) for t in range(training_period)]
    validate_dates = [get_name(training_period + t) for t in range(period)]
    retrain_dates = [get_name(period + t) for t in range(training_period)]
    test_dates = [get_name(training_period + period + t) for t in range(period)]

    pipeline = create_pipeline(train_dates, validate_dates, retrain_dates, test_dates)

    dataset = transform(pagecount).sample(0.05).repartition(32)
    dataset.cache()
    view = dataset.columns[:5] + [F.lit("...")] + dataset.columns[-5:]
    dataset.select(*view).printSchema()

    window = (
        pipeline.fit(dataset)
        .transform(dataset)
        .selectExpr("page_id", "train", "validate", "retrain", "test")
    )
    window.cache()
    window.printSchema()

    observations = train_fit_glmm(window, validate_dates[0])
    observations.cache()
    observations.show()

    # print(f"rmse: {rmse_df(observations, test_dates[0])}")
    # print(f"mape: {mape_df(observations, test_dates[0])}")


if __name__ == "__maFin__":
    main.entry_point()
