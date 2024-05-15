#!/usr/bin/env python3
"""
    Shuffle_data function
"""

import numpy as np


def shuffle_data(X, Y):
    """
        Shuffles the data points in two matrices the same way
    """

    m = len(X)
    permutation = np.random.permutation(m)
    x = X[permutation]
    y = Y[permutation]

    return x, y
