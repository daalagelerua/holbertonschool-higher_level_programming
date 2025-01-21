#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, padding with 0 if necessary
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Use only the first 2 elements of each tuple
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    # Calculate the sum of corresponding elements
    result = (a1 + b1, a2 + b2)

    return result
