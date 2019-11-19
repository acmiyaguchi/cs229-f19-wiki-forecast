# Wikipedia Pageview Forecasting

A machine learning project for CS229 Fall '19.

## Quickstart

### Checkout the repository

```bash
git clone --recursive https://github.com/acmiyaguchi/cs229-f19-wiki-forecast.git

# if you have already checked out the repo and need to initialize submodules
git submodule update --init --recursive
```

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

### Quickstart

## Installing dependencies
This repository uses [Pipenv](https://docs.pipenv.org/en/latest/) for managing
the relevant Python dependencies and installing Spark.

```bash
# install dependencies
pipenv sync --dev

# start the virtual environment
pipenv shell
```

## Running the experiments

Topic-specific sample data is available directly in the repository for testing.
To run the command on the sample data, run the following command on at the project root.

```
python -m wikicast baseline
```

This section of the codebase is pure python.

Download the data for running the full-scale experiment. The following folders should exist under the `data/` directory.

```
data/enwiki/pages/
data/enwiki/pagelinks/
data/enwiki/pagecount_daily_v2/
```

Run the following commands to run the experiments on a graph sampled randomly from articles with a connectivity contraint. This is typically around 35,000 articles. 

```
# in bash on Linux or MacOS
scripts/run-command baseline_random

# in powershell on Windows
scripts/run-command.ps1 baseline_random
```

This requires Java 1.8 to run. Spark is installed from pip, and GraphFrames are installed from spark-packages.


## Running Jupyter with Spark and GraphFrames

Once in the shell, several spark variables should be set to keep the working
environment consistent across machines. For convenience, run one of the following commands.

```bash
# in bash on Linux or MacOS
scripts/start-jupyter`

# in powershell on Windows
scripts/start-jupyter.ps1
```
