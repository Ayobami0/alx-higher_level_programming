#!/usr/bin/python3
"""This module contains an implementation of the Square class."""


class Square:
    """The Square class.

    Instantiates the class with a private field of _size
    """

    def __init__(self, size):
        """Initialize the class.

        Sets the class private attr to the parameter size

        Args:
            size: the size of the size of the Square
        """
        self._size = size
