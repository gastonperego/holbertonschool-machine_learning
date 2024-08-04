#!/usr/bin/env python3
"""
    mat_mul: Performs matrix multiplication
"""


def mat_mul(mat1, mat2):
    """
        Returns a new matrix, being this the product of the two matrices given
    """
    if not len(mat1[0]) == len(mat2):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        new_array = []
        for j in range(len(mat2[0])):
            num = 0
            for k in range(len(mat2)):
                num += mat1[i][k] * mat2[k][j]
            new_array.append(num)
        new_matrix.append(new_array)
    return new_matrix
