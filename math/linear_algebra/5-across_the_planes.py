#!/usr/bin/env python3
"""
    add_matrices: Returns the element wise sum of 2 matrices
"""


def add_matrices2D(mat1, mat2):
    """
        Returns a new matrix that is the element wise sum of 2 matrices
        If the martices are not of the same shape, returns None
    """
    if not len(mat1) == len(mat2) or not len(mat1[0]) == len(mat2[0]):
        return None
    new_matrix = []
    for row1, row2 in zip(mat1, mat2):
        new_row = []
        for el1, el2 in zip(row1, row2):
            new_row.append(el1 + el2)
        new_matrix.append(new_row)

    return new_matrix
