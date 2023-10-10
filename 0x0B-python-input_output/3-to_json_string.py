#!/usr/bin/python3
"""A module module containing a function."""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON string representation.

    Args:
        my_obj (any): The Python object to be converted to a JSON string.

    Returns:
        str: The JSON string representation of the provided object.
    """
    return json.dumps(my_obj)
