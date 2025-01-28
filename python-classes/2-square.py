#!/usr/bin/python3
"""
This module defines the square class.

Classes:
    Square: A class that represents a square.

Exceptions:
    TypeError: Raised when the size is not an integer.
    ValueError: Raised when the size is negative.
"""


class Square:
    """
    This is a class that defines a square

    Attributes: The class 'square' takes a private attribute 'size'
    size must be a positive integer.
    """    
    def __init__(self, size=0):
        """This function initializes a square with optional size 

        Args:
            size (int, optional): size of a square. Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        