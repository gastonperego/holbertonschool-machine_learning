#!/usr/bin/env python3
"""
    Calculate loss function
"""

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()


def calculate_loss(y, y_pred):
    """
        Calculates the softmax cross-entropy loss of a prediction
    """
    return tf.losses.softmax_cross_entropy(y, y_pred)
