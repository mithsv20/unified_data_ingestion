import os
from src.spark_utils import init_spark
from src.json_parser import load_config
from src.reads import read_data
from src.transformations import perform_transformations
from src.writes import write_data


def main():
    """
    Main function to execute the PySpark framework.

    This function loads the configuration, initializes the Spark session,
    reads data, performs transformations, and writes the final output
    to specified formats.
    """
    # Load configuration
    config_path = os.path.join('config', 'config.json')
    config = load_config(config_path)

    # Initialize Spark session
    spark = init_spark(config['spark']['app_name'], config['spark']['master'])

    # Read DataFrames dynamically and create temporary views
    read_data(spark, config['reads'])

    # Perform Transformations
    final_df = perform_transformations(spark, config['transformations'])

    # Write Data for each specified output configuration
    write_data(final_df, config['writes'])

    # Stop Spark session
    spark.stop()


if __name__ == "__main__":
    main()
