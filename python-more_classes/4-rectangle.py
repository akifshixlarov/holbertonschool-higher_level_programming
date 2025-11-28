#!/usr/bin/python3
"""defines a Rectangle class with width, height, area and perimeter"""


class Rectangle:
    """Rectangle class with private width and height"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return printable rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_rows = []
        for _ in range(self.__height):
            rectangle_rows.append("#" * self.__width)

        return "\n".join(rectangle_rows)

    def __repr__(self):
        """Return string representation to recreate a new instance."""
        return "Rectangle({}, {})".format(self.width, self.height)
