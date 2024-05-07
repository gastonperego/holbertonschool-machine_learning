#!/usr/bin/env python3
"""
    One hot encode function
"""

import numpy as np


def one_hot_encode(Y, classes):
    """
        converts a numeric label vector into a one-hot matrix
    """
    one_hot = np.zeros((len(Y), classes))
    for i in range(len(Y)):
        one_hot[i][Y[i]] = 1
    return one_hot.T
