#!/usr/bin/env python3
"""
    Specifity function
"""

import numpy as np


def specificity(confusion):
    """
        Calculates the specifity of each class of a confusion matrix
    """
    precision = []
    copy = confusion.copy()
    copy2 = confusion.copy()
    for i in range(confusion.shape[0]):
        copy[i] = np.zeros(copy[i].shape)
        copy = copy.T
        copy[i] = np.zeros(copy[i].shape)
        copy = copy.T
        copy2[i] = np.zeros(copy2[i].shape)
        precision.append(copy.sum() / copy2.sum())
        copy = confusion.copy()
        copy2 = confusion.copy()

    return np.array(precision)
