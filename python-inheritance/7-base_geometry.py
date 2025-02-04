#!/usr/bin/python3
"""
This is a class that define a function area
"""


class BaseGeometry:
    """
    This class has a function
    """
    def area(self):
        """
        This function raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function checks if value is a positive integer
        Args:
            name (string): name of
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
