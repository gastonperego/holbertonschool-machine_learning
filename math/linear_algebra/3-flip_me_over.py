#!/usr/bin/env python3
"""
    Task 3
"""


def matrix_transpose(matrix):
    new_matrix = []

    for j in range(len(matrix[0])):
        array = []
        for i in range(len(matrix)):
            array.append(matrix[i][j])
        new_matrix.append(array)

    return new_matrix
