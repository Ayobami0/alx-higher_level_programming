#!/usr/bin/python3
"""A module module containing a function that reads a file."""


def read_file(filename=""):
    """Read and print the contents of a file.

    Args:
        filename (str): The name of the file to read
        (default is an empty string).
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read().strip())
