#!/usr/bin/python3
"""A module module containing a function."""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to its corresponding Python object.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
