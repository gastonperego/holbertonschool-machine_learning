#!/usr/bin/env python3
"""
    Task 8
"""


def mat_mul(mat1, mat2):
    """
        Performs matrix multiplication
    """

    if len(mat1[0]) != len(mat2):
        return None

    new_matrix = []

    for i in range(len(mat1)):
        array = []
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                if len(array) <= j:
                    array.append(mat1[i][k] * mat2[k][j])
                else:
                    array[len(array) - 1] += mat1[i][k] * mat2[k][j]
        new_matrix.append(array)

    return new_matrix
