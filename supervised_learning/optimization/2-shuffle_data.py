#!/usr/bin/env python3
"""
    Shuffle_data function
"""

import numpy as np


def shuffle_data(X, Y):
    """
        Shuffles the data points in two matrices the same way
    """

    return np.random.permutation(X), np.random.permutation(Y)
