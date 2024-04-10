#!/usr/bin/env python3

def matrix_shape(matrix):
    array = []

    if len(matrix) > 1:
        array.append(len(matrix))

    array.append(len(matrix[0]))
    if not isinstance(matrix[0][0], int):
        array.append(len(matrix[0][0]))

    return array
