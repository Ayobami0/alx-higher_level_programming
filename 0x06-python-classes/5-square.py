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
        self._size = size  #: size of square

    def area(self):
        """Computes the area of the square.

        An instance method that computes the area of the square
        and return its value
        """
        return self._size**2

    @property
    def size(self):
        """The size property.

        Returns the size instance attr.
        """
        return self._size

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
        self._size = value

    def my_print(self):
        """Prints out the square grid.

        Prints out the square using the '#' character.
        If the size of the square is 0 nothing is printed
        """
        if self._size == 0:
            print("")
        else:
            for _ in range(self._size):
                print("#" * self._size)
