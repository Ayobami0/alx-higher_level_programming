#!/usr/bin/python3
"""This module contains a function that prints a square.

The function will be tested using the similarly named
text file in the tests folder.
You can run the test using this command
    python3 -m doctest -v ./tests/4-print_square.txt
"""


def print_square(size):
    """Print a square.

    This function prints a square of a given size using the `#` character.
    Args:
        size of the square
    Return:
        None
    Raises:
        TypeError:
            size must be an int or a float greater than 0
        ValueError:
            size must be greater or equal to zero
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
