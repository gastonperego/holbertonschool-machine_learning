#!/usr/bin/env python3
"""
    Create confuison matrix function
"""

import numpy as np


def create_confusion_matrix(labels, logits):
    """
        Creates a confusion matrix
    """
    confusion = np.zeros((labels.shape[1], labels.shape[1]))
    for i in range(labels.shape[0]):
        confusion[np.argmax(labels[i])][np.argmax(logits[i])] += 1
    return confusion
