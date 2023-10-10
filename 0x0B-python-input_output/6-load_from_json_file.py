import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file from which
        to load the Python object.

    Returns:
        any: The Python object loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as j:
        return json.load(j)
