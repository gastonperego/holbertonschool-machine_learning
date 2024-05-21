#!/usr/bin/env python3
"""
    F1 score function
"""

import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
        Calculates the f1 score for each class of a confusion matrid
    """
    f1_score = []
    for i in range(confusion.shape[0]):
        f1_score.append(
            (2 * confusion[i][i]) / (2 * confusion[i][i]
                                     + (confusion[i].sum()
                                        - confusion[i][i])
                                     + (confusion.T[i].sum()
                                        - confusion[i][i])))

    return np.array(f1_score)
