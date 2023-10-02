#!/usr/bin/python3
"""This module contains a function that prints the fullname.

The function will be tested using the similarly named
text file in the tests folder.
You can run the test using this command
    python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
"""


def say_my_name(first_name, last_name=""):
    """Print the first name and last name.

    Args:
        first_name: first name
        last_name: last name
    Return:
        None
    Raises:
        TypeError: Both the first name and last name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
