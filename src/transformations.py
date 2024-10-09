from pyspark.sql import SparkSession



def perform_transformations(spark: SparkSession, transformations: list):
    """
    Performs a series of SQL transformations on DataFrames.

    Args:
        spark (SparkSession): The active Spark session.
        transformations (list): A list of dictionaries containing transformation queries and view names.

    Returns:
        DataFrame: The final DataFrame after all transformations.

    This function executes each transformation query in the provided list,
    creating or replacing temporary views as specified.
    """
    last_df = None
    for transform in transformations:
        query = transform['query']
        view_name = transform['view_name']

        if last_df is None:
            last_df = spark.sql(query)
        else:
            last_df.createOrReplaceTempView(view_name)
            last_df = spark.sql(query.replace("filtered_input", view_name).replace("filtered_another", view_name))

        last_df.createOrReplaceTempView(view_name)

    return last_df
