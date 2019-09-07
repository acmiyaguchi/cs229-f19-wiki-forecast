```bash
spark-submit \
    --class ch.epfl.lts2.wikipedia.DumpProcessor \
    --master 'local[*]' \
    --executor-memory 4g \
    --driver-memory 4g \
    --packages \
        org.rogach:scallop_2.11:3.1.5,com.datastax.spark:spark-cassandra-connector_2.11:2.4.0 \
    target/scala-2.11/sparkwiki_2.11-0.9.6.jar \
        --dumpPath data/bzipped \
        --outputPath data/processed \
        --namePrefix enwiki-20190820
```

The format is kind of meh, but it seems to be appropriate for their use-cases. This
dumps out several csv files with the following schema.

```bash
$ tree -d data/processed

data/processed/
├── categorylinks
├── page
│   ├── category_pages
│   └── normal_pages
└── pagelinks
```

```python
>>> spark.read.csv(
    "data/processed/categorylinks",
    sep="\t",
    schema="start_id INT,name STRING,end_id INT,type STRING"
).show(n=5)
+--------+--------------------+--------+------+
|start_id|                name|  end_id|  type|
+--------+--------------------+--------+------+
| 2137402|1000_V_DC_railway...|57839957|subcat|
|51991420|1000_V_DC_railway...|57839957|  page|
|25064564|1000_V_DC_railway...|57839957|  page|
|57839948|1000_V_DC_railway...|57839957|subcat|
|   60340|1000_V_DC_railway...|57839957|  page|
+--------+--------------------+--------+------+

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
