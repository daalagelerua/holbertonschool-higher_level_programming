#!/usr/bin/python3
"""
This module defines a class that inherits from another class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class define a square that inherits from the class rectangle

    Args:
        Rectangle (): class
    """
    def __init__(self, size):
        """
        This function initializes 'size'
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.
        Returns:
            int: the area (size ** 2)
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
