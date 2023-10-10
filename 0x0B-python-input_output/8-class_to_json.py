#!/usr/bin/python3
"""A module module containing a function."""


def class_to_json(obj):
    """
    Convert a class instance to a JSON-serializable dictionary.

    Args:
        obj (object): The instance of a class to be converted to a dictionary.

    Returns:
        dict: A dictionary representation of the class instance.
    """
    dict_rep = {}
    for k, v in obj.__dict__.items():
        if type(k) not in [str, dict, int, list, bool, float]:
            dict_rep[k] = str(v)
        else:
            dict_rep[k] = v
    return dict_rep
