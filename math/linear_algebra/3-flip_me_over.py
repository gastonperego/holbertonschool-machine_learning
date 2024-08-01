#!/usr/bin/env python3
"""
    matrix_transpose: Returns a transposed 2D matrix
"""


def matrix_transpose(matrix):
    """
        Returns a transposed 2D matrix
    """
    new_matrix = []
    for i in range(len(matrix[0])):
        array = []
        for j in range(len(matrix)):
            array.append(matrix[j][i])
        new_matrix.append(array)
    return new_matrix
