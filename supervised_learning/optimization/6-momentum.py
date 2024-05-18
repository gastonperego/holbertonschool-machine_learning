#!/usr/bin/env python3
"""
    Update_variables_momentum function
"""

import tensorflow as tf


def create_momentum_op(alpha, beta1):
    """

    """
    return tf.keras.optimizers.SGD(learning_rate=alpha, momentum=beta1)
