
# If you run into `The system cannot find the path specified.`, then set
# the system environment for JAVA_HOME to point to the Java SDK e.g.
# $env:JAVA_HOME = "C:\Program Files\Java\jdk1.8.0_162"

$env:SPARK_HOME = $(python -c "import pyspark; print(pyspark.__path__[0])")
$env:PYSPARK_DRIVER_PYTHON = "jupyter"
$env:PYSPARK_DRIVER_PYTHON_OPTS = "notebook"


pyspark `
    --master 'local[*]' `
    --conf spark.driver.memory=4g `
    --conf spark.executor.memory=2g `
    --packages `
    graphframes:graphframes:0.7.0-spark2.4-s_2.11
