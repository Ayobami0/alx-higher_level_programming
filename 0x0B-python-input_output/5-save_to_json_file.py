#!/usr/bin/python3
"""A module module containing a function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object as JSON to a file.

    Args:
        my_obj (any): The Python object to be saved as JSON.
        filename (str): The name of the file to which the JSON data
            will be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
