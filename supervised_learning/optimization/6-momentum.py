#!/usr/bin/env python3
"""
    Update_variables_momentum function
"""

import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_eager_execution()


def create_momentum_op(alpha, beta1):
    """

    """
    return tf.keras.optimizers.SGD(learning_rate=alpha, momentum=beta1)
