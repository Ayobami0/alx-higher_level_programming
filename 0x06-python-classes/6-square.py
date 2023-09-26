#!/usr/bin/python3
"""This module contains an implementation of the Square class."""


class Square:
    """A Square class that has a size parameter.

    Sets the class private attr to the parameter size.
    The size variable must be an integer and  must be greater than 0 else
    TypeError and ValueError are raised respectively

    Args:
        size (int): the size of the Square.
        position (:obj:`tuple` of :obj:`int`):  The position to print the
            square.
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        for i in position:
            if type(i) is not int or i < 0:
                raise TypeError(
                    "position must \
be a tuple of 2 positive integers"
                )
        self.__size = size  #: size of square
        self.__position = position  #: print position of square

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

    @property
    def position(self):
        """The position property getter.

        Returns the size instance attr.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """A setter for the position property in the Square class.

        Sets the class private attr to the parameter position.
        The position must be a tuple of integer and  must be greater
        or equal to 0 else TypeError is raised.

        Args:
            value (:obj:`tuple` of :obj:`int`):  The position to print the
                square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__position = value

    def my_print(self):
        """Prints out the square grid.

        Prints out the square using the '#' character.
        If the size of the square is 0 nothing is printed, if the
        postion tuple is empty
        """
        if self.__size == 0:
            print("")
        else:
            print(" " * self.__position[1])
            for _ in range(self.__size):
                print(" " * self.__position[0], "#" * self.__size, sep="")
