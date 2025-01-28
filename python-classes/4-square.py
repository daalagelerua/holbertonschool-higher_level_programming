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
        
        
    def area(self):
        """
        This function returns the area of a square 
        """    
        return self.__size ** 2
    
    @property
    def size(self):
        """
        Getter the size of the square

        Returns:
            int: the size of the square 
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square

        Args:
            value (int): the new size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value