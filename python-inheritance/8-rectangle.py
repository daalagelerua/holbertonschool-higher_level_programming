#!/usr/bin/python3
base_geometry = __import__('7-base_geometry')
BaseGeometry = base_geometry.BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry
    Attributes:
        width: width of rectangle
        height: height of rectangle
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance with width and height

        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        Raises:
        TypeError: If width or height are not integers.
        ValueError: If width or height are less or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height
