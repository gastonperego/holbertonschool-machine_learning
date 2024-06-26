#!/usr/bin/env python3
"""
    Create placeholders function
"""

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
        Creates the forward propagation graph for the neural network
    """
    for i in range(len(layer_sizes)):
        x = create_layer(x, layer_sizes[i], activations[i])

    return x
