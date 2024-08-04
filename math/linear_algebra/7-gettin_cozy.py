#!/usr/bin/env python3
"""
    cat_matrices: Concatenates two 2d matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
        Returns a new matrix, being this the concatenation of two 2d matrices
        along a speceific axis
        If the matrices are not concatenable, retunrs None
    """
    new_matrix = []
    for row in mat1:
        new_matrix.append(row.copy())
    if axis == 0:
        if not len(mat1[0]) == len(mat2[0]):
            return None
        new_matrix += mat2.copy()
    elif axis == 1:
        if not len(mat1) == len(mat2):
            return None
        for i in range(len(new_matrix)):
            new_matrix[i].append(mat2[i][0])
    else:
        return None
    return new_matrix
