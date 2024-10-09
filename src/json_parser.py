import json


def load_config(json_path: str) -> dict:
    """
    Loads the configuration from a JSON file.

    Args:
        json_path (str): The path to the JSON configuration file.

    Returns:
        dict: The loaded configuration as a dictionary.
    """
    with open(json_path, 'r') as file:
        config = json.load(file)
    return config
