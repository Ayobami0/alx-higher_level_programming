#!/usr/bin/python3
"""This module contains a function that adds 2 integers"""


def add_integer(a, b=98):
    """Function to sum up to numbers.

    Args:
        a: an integer or float
        b: an integer or float (has a default value of 98)

    Return:
        The result of the addition

    Raises:
        TypeError: a and b must both of interger types.
    """
    if a is not int or a is not float:
        raise TypeError("a must be an integer")
    if b is not int or b is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
