# Notes

```bash
spark-submit \
    --class ch.epfl.lts2.wikipedia.DumpProcessor \
    --master 'local[*]' \
    --executor-memory 4g \
    --driver-memory 4g \
    --packages \
        org.rogach:scallop_2.11:3.1.5,com.datastax.spark:spark-cassandra-connector_2.11:2.4.0 \
    sparkwiki/target/scala-2.11/sparkwiki_2.11-0.9.6.jar \
        --dumpPath data/bzipped \
        --outputPath data/processed \
        --namePrefix enwiki-20190820
```

```bash
pipenv shell
python -m site
# choose the location of the local site-packages

export SPARK_HOME=$(python -c "import pyspark as _; print(_.__path__[0])")
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS=notebook
pyspark \
    --conf spark.driver.memory=4g \
    --conf spark.executor.memory=4g
```

```bash
spark-submit \
    --class ch.epfl.lts2.wikipedia.DumpParser \
    --master 'local[*]' \
    --executor-memory 4g \
    --driver-memory 4g \
    --packages \
        org.rogach:scallop_2.11:3.1.5,com.datastax.spark:spark-cassandra-connector_2.11:2.4.0 \
    sparkwiki/target/scala-2.11/sparkwiki_2.11-0.9.6.jar \
        --dumpFilePath data/bzipped/enwiki-20190820-page.sql.bz2 \
        --dumpType page \
        --outputPath data/processed/pagecount \
        --outputFormat parquet
```

Run a cassandra daemon for processing pageviews

```bash
docker run \
    -p 9042:9042 \
    -d cassandra:latest
```

```python
from datetime import datetime as dt, timedelta

input = "2019-08-20"
days = 512

fmt = "%Y-%m-%d"
end = dt.strptime(input, fmt)
start = end - timedelta(days)
print(dt.strftime(start, fmt))
```

```
wget -r -np -nH --cut-dirs=3 https://dumps.wikimedia.org/other/pagecounts-ez/merged/2018/
wget -r -np -nH --cut-dirs=3 https://dumps.wikimedia.org/other/pagecounts-ez/merged/2019/

```

```
spark-submit \
    --class ch.epfl.lts2.wikipedia.PagecountProcessor \
    --master 'local[*]' \
    --executor-memory 4g \
    --driver-memory 4g \
    --packages \
        org.rogach:scallop_2.11:3.1.5,com.datastax.spark:spark-cassandra-connector_2.11:2.4.0,com.typesafe:config:1.2.1 \
    sparkwiki/target/scala-2.11/sparkwiki_2.11-0.9.6.jar \
        --config sparkwiki/config/pagecount.conf \
        --basePath data/processed/pagecount-cassandra \
        --pageDump data/processed/pagecount \
        --startDate 2018-03-26 \
        --endDate 2019-08-20
```