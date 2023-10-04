#!/usr/bin/python3
"""This module contains a function that devides all elements of a matrix.

The matrix_divided function will be tested using the similarly named
text file in the tests folder.
You can run the test using this command
    python3 -m doctest -v ./tests/1-matrix_divided.txt | tail -2
"""


def matrix_divided(matrix, div):
    """Function to divide elements of a matrix.

    Args:
        matrix: A list or lists representing a matirx
        div: number to divide the elements
    Return:
        The result of the division in a matrix of the same size
        as the divided matrix.
        The values of the matrix should all be rounded up to two
        decimal places.
        The matrix will be returned if the matric is empty
    Raises:
        TypeError:
            matrix must be a list of list containing integer or float values
            div must both of integer type.
            each row of matrix must be of same size
        ZeroDivisionError:
            div cannot be equal to 0
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists)\
 of integers/floats"
        )
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        return matrix
    len_row = len(matrix[0])
    matrix_cpy = matrix[:]
    for row_idx, row in enumerate(matrix_cpy):
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists)\
 of integers/floats"
            )
        if len(row) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
        for val_idx, val in enumerate(row):
            if type(val) not in [float, int]:
                raise TypeError(
                    "matrix must be a matrix (list of lists)\
 of integers/floats"
                )
            row[val_idx] = round(val / div, 2)
        matrix_cpy[row_idx] = row
    return matrix_cpy
