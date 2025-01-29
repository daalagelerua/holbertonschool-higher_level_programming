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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with optional size

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: if size is less than 0
        """

        self.size = size
        self.position = position

    def area(self):
        """
        This function returns the area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for the size of the square

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

    def my_print(self):
        """
        Print a square.

        if size is 0, print an empty line
        The position is respected by adding spaces and empty lines.
        """

        if self.size == 0:
            print()
            return

        print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0] + '#' * self.size)

    @property
    def position(self):
        """
        getter for the position of the square.

        returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers
            representing the position.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2
           or not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
