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
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle of optional width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        
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
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")
    
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
    if not isinstance(height, int):
        raise TypeError("height must be an integer")
    if height < 0:
        raise ValueError("height must be >= 0")
