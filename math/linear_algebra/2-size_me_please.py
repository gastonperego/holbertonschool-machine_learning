#!/usr/bin/env python3
"""
    Task 2
"""
def matrix_shape(matrix):
    """
        Function that returns the shape of a given matrix
    """
    array = []

    recursive(matrix, array)
    return array


def recursive(matrix, array):
    """
        Recursive function that appends the length of the nested arrays
    """
    if not isinstance(matrix, int):
        array.append(len(matrix))
        recursive(matrix[0], array)

    return array
