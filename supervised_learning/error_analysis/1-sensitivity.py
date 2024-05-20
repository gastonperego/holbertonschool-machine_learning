#!/usr/bin/env python3
"""
    Sensitivity function
"""

import numpy as np


def sensitivity(confusion):
    """
        Calculates the sensitivity of each class of a confusion matrix
    """
    sensitivity = []
    for i in range(confusion.shape[0]):
        sensitivity.append(confusion[i][i] / confusion[i].sum())

    return np.array(sensitivity)
