#!/usr/bin/env python3
"""
    Task 7
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
        Concatenares 2 matrices along a specific axis
    """

    new_matrix = []
    for row in mat1:
        new_matrix.append(row.copy())
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        for row in mat2:
            new_matrix.append(row)
        return new_matrix
    elif axis == 1 and len(mat1) == len(mat2):
        for i in range(len(mat2)):
            new_matrix[i] += mat2[i]
        return new_matrix
    else:
        return None
