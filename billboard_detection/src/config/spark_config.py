from pyspark.sql import SparkSession

def create_spark_session(app_name="BillboardDetection"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.some.config.option", "config-value") \
        .getOrCreate()
    return spark

def get_spark_config():
    return {
        "spark.master": "local[*]",
        "spark.executor.memory": "4g",
        "spark.driver.memory": "2g",
        "spark.sql.shuffle.partitions": "200"
    }