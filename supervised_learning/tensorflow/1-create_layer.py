#!/usr/bin/env python3
"""
    Create placeholders function
"""

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()


def create_layer(prev, n, activation):
    """
        Creates a layer of the neural network
    """
    initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layer = tf.keras.layers.Dense(units=n, kernel_initializer=initializer,
                                  activation=activation, name='layer')

    return layer(prev)
