#!/usr/bin/python3
"""This module contains an implementation of the Square class.

    The class does nothig for now.
"""


class Square:
    """A Square class that has a size parameter.

    Sets the class private attr to the parameter size.
    The size variable must be an integer and  must be greater than 0 else
    TypeError and ValueError are raised respectively

    Args:
        size (int): the size of the Square.
    """

    def __init__(self, size):
        self._size = size
