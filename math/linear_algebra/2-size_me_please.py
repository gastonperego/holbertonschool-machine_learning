#!/usr/bin/env python3
"""
    matrix_shape: Calculates the shape of a matrix
"""
def matrix_shape(matrix):
    
    shape = []
    while (not isinstance(matrix, int)):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape