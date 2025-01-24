from pyspark.sql import SparkSession

def create_spark_session():
    return SparkSession.builder \
        .appName("BillboardDetection") \
        .config("spark.executor.memory", "16g") \
        .config("spark.driver.memory", "8g") \
        .config("spark.executor.cores", "4") \
        .getOrCreate()