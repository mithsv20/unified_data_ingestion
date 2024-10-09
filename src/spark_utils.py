from pyspark.sql import SparkSession


def init_spark(app_name: str, master: str) -> SparkSession:
    """
    Initializes a Spark session.

    Args:
        app_name (str): The name of the Spark application.
        master (str): The master URL for the Spark cluster.

    Returns:
        SparkSession: A Spark session instance.
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .master(master) \
        .getOrCreate()
    return spark
