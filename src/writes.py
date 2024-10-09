from pyspark.sql import DataFrame


def write_data(df: DataFrame, write_configs: list):
    """
    Writes the DataFrame to specified output formats and paths.

    Args:
        df (DataFrame): The DataFrame to be written.
        write_configs (list): A list of dictionaries containing write configurations.

    This function writes the DataFrame to the specified locations
    in the formats defined in the configuration.
    """
    for write_config in write_configs:
        df.createOrReplaceTempView(write_config['view_name'])
        df.write.format(write_config['format']).mode(write_config['mode']).save(write_config['path'])
