#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
     A class that defines a square.

    Attributes:
        size (int): The size of the square's side.
    """

    def __init__(self, size=0):
        """
        Initializes a square with optonal size

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: if size is less than 0
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        """
        This function returns the area of a square 
        """    
        return self.__size ** 2