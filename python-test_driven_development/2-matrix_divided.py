#!/usr/bin/python3
"""
Function divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of lists
        div: int or float

    Return:
        new_matrix

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        ZeroDivisionError: Each row of the matrix must have the same size
    """
    new_matrix = []
    error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    error_2 = "Each row of the matrix must have the same size"

    if not isinstance(matrix, (list)):
        raise TypeError()
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(error_2)
        new_row = []
        for index in row:
            if not isinstance(index, (int, float)):
                raise TypeError(error_1)
            else:
                new_row.append(round(index / div, 2))
        new_matrix.append(new_row)
    return new_matrix
