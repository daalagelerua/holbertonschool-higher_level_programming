#!/usr/bin/python3
"""
This module defines a function to divide each elements of a matrix.

The function `matrix_divided` takes a matrix and a divisor,
and returns a new matrix with all elements divided by the divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The divisor.

    Returns:
    list of lists of float: The new matrix with all elements divided by div.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats.
    TypeError: If each row of the matrix is not of the same size.
    TypeError: If div is not a number (integer or float).
    ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
