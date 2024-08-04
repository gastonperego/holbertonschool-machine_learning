#!/usr/bin/env python3
"""
    np_cat: Concatenates 2 matries along a specific axis
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
        Returns a new np.ndarray that is the concatenations of the 2 matrices
        along the specified axis
    """
    array = np.concat([mat1, mat2], axis) 
    return array
