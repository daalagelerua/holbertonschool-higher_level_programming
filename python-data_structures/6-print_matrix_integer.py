#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if column == len(matrix[row]) - 1:  # if last element of row
                print("{:d}".format(matrix[row][column]), end='')
            else:
                print("{:d}".format(matrix[row][column]), end=' ')
        print()
