#!/usr/bin/python3
"""A module module containing a function."""


def append_write(filename="", text=""):
    """
    Append the provided text to an existing file or create a
    new file if it doesn't exist.

    Args:
        filename (str): The name of the file to append to (default
            is an empty string).
        text (str): The text to be appended to the file (default
            is an empty string).

    Note:
        If 'filename' is not provided or is an empty string, or if
        'text' is not provided,
        the function will not append anything to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
