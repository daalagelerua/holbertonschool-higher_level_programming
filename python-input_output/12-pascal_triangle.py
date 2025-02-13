#!/usr/bin/python3
"""
This module defines a function that print a pascal triangle
"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                # Calculate the value based on the previous row
                value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(value)
        triangle.append(current_row)
    
    return triangle