#!/usr/bin/python3
"""
This module define a class with a function to check
the area
"""


class BaseGeometry:
    """
    This class has a function to check the area
    """

    def area(self):
        """
        This function raises an exception if the area
        is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function checks if value is a positive integer

        Args:
            name (string): name of
            value (int): value
        
        Raises:
            TypeError: If value is not integer
            ValueError: If value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
