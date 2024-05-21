#!/usr/bin/env python3
"""
    Precision function
"""

import numpy as np


def precision(confusion):
    """
        Calculates the precision of each class of a confusion matrix
    """
    precision = []
    copy = confusion.copy()
    for i in range(confusion.shape[0]):
        precision.append(confusion[i][i] / confusion.T[i].sum())

    return precision
