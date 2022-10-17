#!/usr/bin/python3
"""
The Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix

    Args:
        matrix: list of lists
        div: integer/float divisor
    """
    if ((not isinstance(div, int)) and (not isinstance(div, float))):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(i, list) for i in matrix) or
            not all((isinstance(j, int) or isinstance(j, float))
            for j in [num for i in matrix for num in i])):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if (not all(len(i) == len(matrix[0]) for i in matrix)):
        raise TypeError('Each row of the matrix must have the same size')

    return ([list(map(lambda x: round(x / div, 2), i)) for i in matrix])
