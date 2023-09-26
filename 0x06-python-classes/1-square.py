#!/usr/bin/python3
"""This module contains an implementation of the Square class."""


class Square:
    """A Square class that has a size parameter.

    Sets the class private attr to the parameter size.

    Args:
        size : the size of the Square.
    """

    def __init__(self, size=0):
        self.__size = size
