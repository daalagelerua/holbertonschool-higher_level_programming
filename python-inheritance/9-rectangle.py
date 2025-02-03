#!/usr/bin/python3
base_geometry = __import__('7-base_geometry')
BaseGeometry = base_geometry.BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry.
    Attributes:
        __width: width of the rectangle.
        __height: height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance with width and height.
        
        Args:
            width (int): width of the rectangle (must be a positive integer).
            height (int): height of the rectangle (must be a positive integer).
        
        Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are less than or equal to 0.
        """
        # Validate the width and height using integer_validator from BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        # Set private attributes with name mangling
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            int: the area (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width} / {self.__height}"

    def __repr__(self):
        """
        Return a formal string representation of the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"
    