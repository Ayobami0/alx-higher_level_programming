#!/usr/bin/python3
"""This module contains a function that adds 2 integers.

The add_integer function will be tested using the similarly named
text file in the tests folder.
You can run the test using this command
    python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
"""


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
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
