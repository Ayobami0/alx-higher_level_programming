"""A module module containing a function that reads a file."""


def read_file(filename=""):
    """Read and print the contents of a file.

    Args:
        filename (str): The name of the file to read
        (default is an empty string).
    Note:
        If 'filename' is not provided or is an empty string,
        the function will not read any file.
    """
    try:
        with open(filename, "r", encoding="UTF8") as f:
            print(f.read())
    except Exception:
        pass
