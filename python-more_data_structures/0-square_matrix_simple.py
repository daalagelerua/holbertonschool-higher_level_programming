#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    squared_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row for the squared matrix
        squared_row = []

        # Iterate over each element in the current row
        for element in row:
            # Square the element and append it to the squared row
            squared_row.append(element ** 2)

        # Append the squared row to the squared matrix
        squared_matrix.append(squared_row)

    # Return the squared matrix
    return squared_matrix
