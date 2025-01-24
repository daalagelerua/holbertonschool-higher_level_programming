#!/usr/bin/python3
'''
This is a function that add 2 integers

This function takes 2 arguments a and b
and returns their sum, casting any float to integers.
'''


def add_integer(a, b=98):
    '''
    Adds 2 integers or float, returning the result as an integer.

    Parameters:
    a (int, float): The first number.
    b (int, float): Second number (default is 98).

    Returns:
    int: the sum of the 2 numbers.

    Raises:
    TypeError: If a or b is not an integer or float.

    Example:
    >>> add_integer(2, 3)
    5
    >>> add_integer(2.5, 3)
    5
    >>> add_integer(2)
    100
    '''
    if type(a) not in [int, float] or a == "nan":
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b == "nan":
        raise TypeError("b must be an integer")
    return int(a) + int(b)
