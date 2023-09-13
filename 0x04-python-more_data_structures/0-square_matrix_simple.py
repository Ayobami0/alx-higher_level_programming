#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    return [list(map(lambda x: x * x, y)) for y in matrix]
