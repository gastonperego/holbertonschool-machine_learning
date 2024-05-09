#!/usr/bin/env python3
"""
    Calculate accurancy function
"""

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()


def calculate_accuracy(y, y_pred):
    """
        calculates the accuracy of a prediction
    """
    y_true = tf.argmax(y, axis=1)
    y_pred_true = tf.argmax(y_pred, axis=1)

    correct_predictions = tf.equal(y_true, y_pred_true)

    accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

    return accuracy
