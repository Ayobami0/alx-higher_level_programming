#!/usr/bin/python3
"""This module contains an implementation of the Square class."""


class Square:
    """A Square class that has a size parameter.

    Sets the class private attr to the parameter size.
    The size variable must be an integer and  must be greater than 0 else
    TypeError and ValueError are raised respectively

    Args:
        size (int): the size of the Square.
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  #: size of square

    def area(self):
        """Computes the area of the square.

        An instance method that computes the area of the square
        and return its value
        """
        return self.__size**2

    @property
    def size(self):
        """The size property.

        Returns the size instance attr.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter for the Square class.

        Sets the class private attr to the parameter size.
        The size variable must be an integer and  must be greater than 0 else
        TypeError and ValueError are raised respectively

        Args:
            value (int): the size of the Square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
