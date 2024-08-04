#!/usr/bin/env python3
"""
    add_arrays: Returns the element wise sum of two arrays of the same size
"""


def add_arrays(arr1, arr2):
    """
        Returns a new array that is the element wise sum of the 2 arrays given
        If the arrays given are not the same size, it returns None
    """
    if not len(arr1) == len(arr2):
        return None
    new_array = []
    for i in range(len(arr1)):
        new_array.append(arr1[i] + arr2[i])

    return new_array
