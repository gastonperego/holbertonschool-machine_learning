#!/usr/bin/env python3
"""
    Task 5
"""


def add_matrices2D(mat1, mat2):
    """
        Adds 2 matrices
    """

    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    sum = []
    for i in range(len(mat1)):
        array = []
        for j in range(len(mat1[0])):
            array.append(mat1[i][j] + mat2[i][j])
        sum.append(array)

    return sum
