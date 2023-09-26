#!/usr/bin/python3
"""This module contains an implementation of the Square class.

    This is a comment and i guess it shoud contain more lines.
"""


class Square:
    """The Square class that probably computes the area of a square.

    Instantiates the class with a private field of _size.
    Instantiates the class with a private field of _size.
    Instantiates the class with a private field of _size.
    """

    def __init__(self, size=0):
        """Initialize the class.

        Sets the class private attr to the parameter size.
        The size variable must be an integer and  must be greater than 0 else
        TypeError and ValueError are raised respectively

        Args:
            size (int): the size of the Square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
