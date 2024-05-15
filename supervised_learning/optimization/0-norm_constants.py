#!/usr/bin/env python3
"""
    Normalization_constants function
"""

import numpy as np


def normalization_constants(X):
    """
        Returns the mean and the standard deviation of each feature
    """

    return np.mean(X, axis=0),  np.std(X, axis=0)
