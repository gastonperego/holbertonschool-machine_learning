#!/usr/bin/env python3
"""
    l2 reg cost function
"""

import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """
        Creates a layer with l2 regularization
    """
    initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    regularizer = tf.keras.regularizers.L2(l2=lambtha)

    layer = tf.keras.layers.Dense(units=n, kernel_initializer=initializer,
                            kernel_regularizer=regularizer,
                            activation=activation)

    return layer(prev)
