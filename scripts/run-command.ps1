
python setup.py bdist_egg
# write the file encoded in utf-8 without BOM
$content = "from wikicast import __main__; __main__.cli()"
$filename = "runner.py"
[IO.File]::WriteAllLines($filename, $content)

$env:SPARK_HOME = $(python -c "import pyspark; print(pyspark.__path__[0])")

spark-submit `
    --master 'local[*]' `
    --conf spark.driver.memory=4g `
    --conf spark.executor.memory=2g `
    --packages graphframes:graphframes:0.7.0-spark2.4-s_2.11 `
    --py-files "dist/*.egg" `
    runner.py @args
