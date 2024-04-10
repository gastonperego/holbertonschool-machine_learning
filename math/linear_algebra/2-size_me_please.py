#!/usr/bin/env python3

def matrix_shape(matrix):
    array = []
    
    recursive(matrix, array)
    return array


def recursive(matrix, array):
    if not isinstance(matrix, int):
        array.append(len(matrix))
        recursive(matrix[0], array) 
        
    return array
