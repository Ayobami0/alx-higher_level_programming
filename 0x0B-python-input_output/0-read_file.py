"""A module module containing a function that reads a file.

read_file(filename="")
"""


def read_file(filename=""):
    """Read and print the contents of a file.

    Args:
        filename (str): The name of the file to read
        (default is an empty string).
    """
    try:
        with open(filename, "r", encoding="UTF8") as f:
            print(f.read())
    except Exception:
        pass
