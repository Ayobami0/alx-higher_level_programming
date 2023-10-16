#!/usr/bin/python3
"""Square module.

It contains the Square class which inherites the imported Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Squaer class representing a square shape.

    Attributes:
        size (int): the size of the square.
        x (int): The x-coordinate position of the top-left corner
            of the square.
        y (int): The y-coordinate position of the top-left corner
            of the square.
        id (int): The ID of the square object.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's
                position (default is 0).
            y (int, optional): The y-coordinate of the square's
                position (default is 0).
            id (int or None, optional): The unique identifier
                for the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """
        Return a string representation of the Square instance.

        Returns:
            str: A string containing class name, id, coordinates,
                and size of the square.
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width,
        )

    @property
    def size(self):
        """
        int: Get the size of the square.
        """
        return self.width

    @size.setter
    def size(self, val):
        """
        Set the size of the square.

        Args:
            val (int): The new size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = val
        self.height = val

    def to_dictionary(self):
        """
        Convert a Square instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the attributes 'y', 'x', 'id',
                and 'size'.

        """
        return {"x": self.x, "y": self.y, "id": self.id, "size": self.size}

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle object.

        The attributes that can be updated include:
          - id
          - size
          - x
          - y

        Args:
            *args: Positional arguments. Can be passed as individual values
                or as a list/tuple with id, width, height, x, y in that order.
            **kwargs: Keyword arguments. Can be passed as key-value
                pairs for id, size, x, y.

        Raises:
            TypeError: If any value is not an integer.
            ValueError: If any value is out of range (size <= 0 or
                x, y < 0).
        """
        if len(args) != 0:
            args = list(args)
            args.extend([None for _ in range(4 - len(args))])
            id, size, x, y = args
        elif len(kwargs) != 0:
            id = kwargs.get("id", None)
            size = kwargs.get("size", None)
            x = kwargs.get("x", None)
            y = kwargs.get("y", None)
        else:
            return

        self.validate(
            (id if id is not None else 1, "id"),
            (size if size is not None else 1, "size"),
            (x if x is not None else 1, "x"),
            (y if y is not None else 1, "y"),
        )
        self.id = id if id is not None else self.id
        self.width = size if size is not None else self.width
        self.x = x if x is not None else self.x
        self.y = y if y is not None else self.y
