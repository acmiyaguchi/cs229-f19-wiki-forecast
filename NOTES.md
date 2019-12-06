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
        --outputPath data/processed/page_parquet \
        --outputFormat parquet
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

```bash
# pagecounts-ez/2019/2019-03/pagecounts-2019-03-13.bz2
# warning, this will take a long time (est 16 hours at 2MB/s)
cd data/raw/pagecounts
wget -c -r -np -nH -R index.html --cut-dirs=5 https://dumps.wikimedia.org/other/pagecounts-ez/merged/2018/
wget -c -r -np -nH -R index.html --cut-dirs=5 https://dumps.wikimedia.org/other/pagecounts-ez/merged/2019/
```

Run a cassandra daemon for processing pageviews

```bash
docker run \
    -p 9042:9042 \
    -d cassandra:latest
```

```SQL
-- DML statements for `cqlsh` connecting to container
CREATE KEYSPACE wikipedia WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

CREATE TABLE wikipedia.page_visits ( page_id bigint, visit_time timestamp, count int, PRIMARY KEY (page_id, visit_time));

CREATE TABLE wikipedia.pagecount_metadata ( start_time timestamp, end_time timestamp, PRIMARY KEY (start_time, end_time));
```

```bash
spark-submit \
    --class ch.epfl.lts2.wikipedia.PagecountProcessor \
    --master 'local[*]' \
    --executor-memory 4g \
    --driver-memory 4g \
    --packages \
        org.rogach:scallop_2.11:3.1.5,com.datastax.spark:spark-cassandra-connector_2.11:2.4.0,com.typesafe:config:1.2.1 \
    sparkwiki/target/scala-2.11/sparkwiki_2.11-0.9.6.jar \
        --config sparkwiki/config/pagecount.conf \
        --basePath data/raw/pagecounts \
        --pageDump data/enwiki/page_parquet \
        --startDate 2019-01-01 \
        --endDate 2019-03-01
```

```bash
SPARK_HOME=$(python -c "import pyspark; print(pyspark.__path__[0])") \
PYSPARK_DRIVER_PYTHON=jupyter \
PYSPARK_DRIVER_PYTHON_OPTS=notebook \
pyspark \
    --conf spark.driver.memory=4g \
    --packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.0
```

```bash
spark-submit \
    --class ch.epfl.lts2.wikipedia.PagecountProcessor \
    --master 'local[*]' \
    --executor-memory 4g \
    --driver-memory 4g \
    --packages \
        org.rogach:scallop_2.11:3.1.5,com.datastax.spark:spark-cassandra-connector_2.11:2.4.0,com.typesafe:config:1.2.1 \
    sparkwiki/target/scala-2.11/sparkwiki_2.11-0.9.6.jar \
        --config sparkwiki/config/pagecount.conf \
        --basePath data/raw/pagecounts \
        --pageDump data/enwiki/page_parquet \
        --outputPath data/processed/pagecount \
        --startDate 2018-01-01 \
        --endDate 2019-09-01
```

```bash
gsutil rsync -d -r enwiki gs://wiki-forecast-data/enwiki
```

```bash
for i in {2..5}; do
    artifact=sample_data/trial_${i}
    scripts/run-command \
        subgraph pageview \
            --artifact-path ${artifact} && \
    python runner.py \
        subgraph summarize-pageview \
            --artifact-path ${artifact}
done
```

```bash
pipenv sync

for i in {1..4}; do
    # rerun a specific trial
    artifact_path="sample_data/trial_$i"
    artifact="--artifact-path $artifact_path"
    seed=$(cat $artifact_path/seed.txt | cut -d, -f1)
    hops=$(cat $artifact_path/seed.txt | cut -d, -f3)
    scripts/run-command subgraph sample --article-seed $seed --k-hops $hops $artifact
    scripts/run-command subgraph summarize-graph $artifact
    scripts/run-command subgraph pageview $artifact
    scripts/run-command subgraph summarize-pageview $artifact
done

for i in {0..6}; do scripts/run-command subgraph pageview --artifact-path sample_data/trial_$i; done
```

```bash
gsutil -m rsync -d -r data/design_matrix gs://wiki-forecast-data/design_matrix
```
