#!/usr/bin/env python3
"""
    One hot encode function
"""

import numpy as np


def one_hot_encode(Y, classes):
    """
        Converts a numeric label vector into a one-hot matrix
    """
    if not isinstance(Y, np.ndarray) or not isinstance(classes, int)\
            or classes < 2:
        return None
    if any([x >= classes for x in Y]):
        return None
    one_hot = np.zeros((len(Y), classes))
    for i in range(len(Y) - 1):
        one_hot[i][Y[i]] = 1
    return one_hot.T
