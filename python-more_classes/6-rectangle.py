#!/usr/bin/python3
"""
This module defines the rectangle class.

Classes:
    Rectangle: A class that represents a rectangle.

"""


class Rectangle:
    """
     This is a class that defines a rectangle.

    Attributes:
    width: The width of the rectangle.
    height: The height of the rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle of optional width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
        TypeError: If height is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This function returns the area of a rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This function returns the perimeter of a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        This function returns the rectangle with #.
        """
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str
        for i in range(self.__height):
            rectangle_str += ("#" * self.__width)
            if i is not (self.__height - 1):
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """
        This function returns a string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        This function delete the rectangle.
        """
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
