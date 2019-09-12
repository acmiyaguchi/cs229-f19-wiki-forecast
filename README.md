# Wikipedia Pageview Forecasting

A machine learning project for CS229 Fall '19.

## Quickstart

### Download the data

The data has been preprocessed into compact Parquet datasets using the
[epfl-ls2/sparkwiki](https://github.com/epfl-lts2/sparkwiki) project. The
Wikipedia SQL dumps from 20190820 and pageviews from 2018-01-01 to 2019-09-01
have been processed.

Contact @acmiyaguchi for access to the cloud storage bucket. If you have been
added to the project, the files may be downloaded via `gsutil`:

```bash
gsutil ls gs://wiki-forecast-data
```

### Running Jupyter and Spark

This repository uses [Pipenv](https://docs.pipenv.org/en/latest/) for managing
the relevant Python dependencies and installing Spark.

```bash
# install dependencies
pipenv sync --dev

# start the virtual environment
pipenv shell
```

Once in the shell, several spark variables should be set to keep the working
environment consistent across machines. For convenience, run
`scripts/start-jupyter`.

```bash
# export variables for local spark package in the site-packages folder
export SPARK_HOME=$(python -c "import pyspark; print(pyspark.__path__[0])")

# start an interactive spark session using python 3.6
pyspark

# Start pyspark using jupyter notebook
PYSPARK_DRIVER_PYTHON=jupyter \
PYSPARK_DRIVER_PYTHON_OPTS=notebook \
pyspark \
    --conf spark.driver.memory=4g \
    --conf spark.executor.memory=4g \
    --packages \
        graphframes:graphframes:0.7.0-spark2.4-s_2.11
```
