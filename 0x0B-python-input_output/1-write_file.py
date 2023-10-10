#!/usr/bin/python3
"""A module module containing a function."""


def write_file(filename="", text=""):
    """
    Write the provided text to a file.

    Args:
        filename (str): The name of the file to write to
            (default is an empty string).
        text (str): The text to be written to the file
            (default is an empty string).

    Note:
        If 'filename' is not provided or is an empty string,
        or if 'text' is not provided, the function
        will not write anything to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
