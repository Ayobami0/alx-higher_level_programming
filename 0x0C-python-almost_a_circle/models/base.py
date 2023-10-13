#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base class with an ID attribute for object identification."""

    __nb_object = 0

    def __init__(self, id) -> None:
        """
        Initialize the Base object with an ID.

        Args:
            id (int): The ID of the object. If None, auto-incremented
                ID is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
