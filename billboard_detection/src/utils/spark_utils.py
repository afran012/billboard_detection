def create_spark_session(app_name):
    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
    
    return spark

def read_data(spark, file_path, file_format='csv', options=None):
    if options is None:
        options = {}
    
    df = spark.read.format(file_format).options(**options).load(file_path)
    return df

def write_data(df, output_path, file_format='csv', options=None):
    if options is None:
        options = {}
    
    df.write.format(file_format).options(**options).save(output_path)

def transform_data(df, transformation_func):
    return transformation_func(df)