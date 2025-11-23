#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix (list of lists): The matrix to print.
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))