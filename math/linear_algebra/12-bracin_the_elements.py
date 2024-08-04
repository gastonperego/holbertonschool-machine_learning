#!/usr/bin/env python3
"""
    np_elementwise: Performs element wise addition, substraction,
    multiplication and division between 2 matrices
"""


def np_elementwise(mat1, mat2):
    """
        Returns a tuple containing the result of the addition, substraction,
        multiplication and division of the 2 matrices
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
