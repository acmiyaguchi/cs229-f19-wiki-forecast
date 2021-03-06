
rm -r dist/
python setup.py bdist_egg
# write the file encoded in utf-8 without BOM
$content = "from wikicast import __main__; __main__.cli()"
$filename = "runner.py"
[IO.File]::WriteAllLines($filename, $content)

$env:SPARK_HOME = $(python -c "import pyspark; print(pyspark.__path__[0])")

spark-submit `
    --master 'local[*]' `
    --conf spark.driver.memory=8g `
    --conf spark.sql.shuffle.partitions=8 `
    --packages graphframes:graphframes:0.7.0-spark2.4-s_2.11 `
    --py-files "dist/*.egg" `
    runner.py @args
