from pyspark.sql import SparkSession


def read_data(spark: SparkSession, read_configs: list):
    """
    Reads data from specified sources and creates temporary views.

    Args:
        spark (SparkSession): The active Spark session.
        read_configs (list): A list of dictionaries containing read configurations.

    This function reads data according to the specified configurations
    and creates temporary views for each dataset.
    """
    for read_config in read_configs:
        read_options = read_config['options']
        df = spark.read.format(read_config['format']).options(**read_options).load(read_config['path'])
        df.createOrReplaceTempView(read_config['view_name'])
