#!/usr/bin/python3
"""Rectangle module.

It contains the rectangle class which inherites the imported base class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle shape.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate position of the top-left corner
            of the rectangle.
        y (int): The y-coordinate position of the top-left corner
            of the rectangle.
        id (int): The ID of the rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """
        Initialize the Rectangle object with width, height, and position.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate position of the top-left corner
                of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate position of the top-left corner
                of the rectangle. Defaults to 0.
            id (int, optional): The ID of the rectangle object.
                Defaults to None.
        """
        super().__init__(id)
        self.validate((width, "width"), (height, "height"), (x, "x"), (y, "y"))
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        int: Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Set the width of the rectangle.

        Args:
            val (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.validate((val, "width"))
        self.__width = val

    @property
    def height(self):
        """
        int: Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Set the height of the rectangle.

        Args:
            val (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.validate((val, "height"))
        self.__height = val

    @property
    def x(self):
        """
        int: Get the x-coordinate position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Set the x-coordinate position of the rectangle.

        Args:
            val (int): The new x-coordinate position value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        self.validate((val, "x"))
        self.__x = val

    @property
    def y(self):
        """
        int: Get the y-coordinate position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Set the y-coordinate position of the rectangle.

        Args:
            val (int): The new y-coordinate position value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        self.validate((val, "y"))
        self.__y = val

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """
        Display a visual representation of the rectangle using "#" symbols.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self) -> str:
        """
        Return a formatted string representation of the rectangle object.

        Returns:
            str: A string representation of the rectangle object.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height,
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle object.

        The attributes that can be updated include:
          - id
          - width
          - height
          - x
          - y

        Args:
            *args: Positional arguments. Can be passed as individual values
                or as a list/tuple with id, width, height, x, y in that order.
            **kwargs: Keyword arguments. Can be passed as key-value
                pairs for id, width, height, x, y.

        Raises:
            TypeError: If any value is not an integer.
            ValueError: If any value is out of range (width, height <= 0 or
                x, y < 0).
        """
        if len(args) != 0:
            args = list(args)
            args.extend([None for _ in range(5 - len(args))])
            id, width, height, x, y = args
        elif len(kwargs) != 0:
            id = kwargs.get("id", None)
            width = kwargs.get("width", None)
            height = kwargs.get("height", None)
            x = kwargs.get("id", None)
            y = kwargs.get("y", None)
        else:
            return

        self.validate(
            (id if id is not None else 1, "id"),
            # This is to allow the validate function set the values
            # even if they are none
            (width if width is not None else 1, "width"),
            (height if height is not None else 1, "height"),
            (x if x is not None else 1, "x"),
            (y if y is not None else 1, "y"),
        )
        self.id = id if id is not None else self.id
        self.__width = width if width is not None else self.__width
        self.__height = height if height is not None else self.__height
        self.__x = x if x is not None else self.__x
        self.__y = y if y is not None else self.__y

    def to_dictionary(
        self,
    ):
        return {
            "y": self.y,
            "x": self.x,
            "id": self.id,
            "width": self.width,
            "height": self.height,
        }

    @staticmethod
    def validate(*args):
        """
        Validate the given arguments.

        Args:
            *args: Variable-length list of tuples. Each tuple contains a value
                and its corresponding name.

        Raises:
            TypeError: If any value is not an integer.
            ValueError: If any value is out of range (width, height <= 0 or
                x, y < 0).
        """
        for v in args:
            if not isinstance(v[0], int):
                raise TypeError("{} must be an integer".format(v[1]))
            if v[1] in ("width", "height") and v[0] <= 0:
                raise ValueError("{} must be > 0".format(v[1]))
            if v[1] in ("x", "y") and v[0] < 0:
                raise ValueError("{} must be >= 0".format(v[1]))
