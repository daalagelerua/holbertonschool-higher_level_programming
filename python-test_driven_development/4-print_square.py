#!/usr/bin/python3
"""
This function `print_square` take an integer,
and print a square of length 'size' made of '#' .
"""


def print_square(size):
    """
    Print a square.

    Parameters:
    size: length of the square.

    Raises:
    ValueError: If size is less than 0.
    TypeError: If size is not an integer.
    TypeError: If size is a float and is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("{}".format('#' * size))
