#!/usr/bin/env python3
"""
    Create train op function
"""

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()


def create_train_op(loss, alpha):
    """
        Creates the training operation for the network
    """

    optimizer = tf.train.GradientDescentOptimizer(alpha)
    train = optimizer.minimize(loss)

    return train
