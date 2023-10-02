#!/usr/bin/python3

"""A module containing a rectangle class.

This class is a representation of a rectangle and tries to
imitate the functionality.
"""


class Rectangle:
    """Represents a rectangle with width and height properties.

    Attributes:
        number_of_instance (int): The number of Rectangle instances created.
        print_symbol (str): The symbol used for printing rectangles.

    Methods:
        __init__(self, width=0, height=0): Initializes a Rectangle instance
            with specified width and height.
        width (property): Gets the width of the rectangle.
        width (setter): Sets the width of the rectangle.
        height (property): Gets the height of the rectangle.
        height (setter): Sets the height of the rectangle.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the
            rectangle using the print_symbol.
        __del__(self): Decrements the number_of_instance when
            a Rectangle instance is deleted.
        bigger_or_equal(rect_1, rect_2): Compares two rectangles
            and returns the larger one.
    """

    number_of_instance = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with specified width and height.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.

        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.number_of_instance += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter value.

        """
        if self.__height == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        str_rep = ""
        for i in range(self.__height):
            str_rep += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                str_rep += "\n"
        return str_rep

    def __del__(self):
        """Decrements the number_of_instance when a Rectangle is deleted."""
        self.number_of_instance -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the larger one.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The larger rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    def __repr__(self):
        """Returns an object representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
