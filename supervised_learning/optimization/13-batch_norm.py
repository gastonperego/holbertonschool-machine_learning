#!/usr/bin/env python3
"""
    Batch_norm function
"""

import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    """
        Normalizes an unactivated output of a neural
        network using batch normalization
    """

    mu = np.mean(Z, axis=0)
    sigma2 = np.var(Z, axis=0)

    z_norm = (Z - mu) / np.sqrt(sigma2 + epsilon)
    z = gamma * z_norm + beta

    return z
