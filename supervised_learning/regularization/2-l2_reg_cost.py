#!/usr/bin/env python3
"""
    l2 reg cost function
"""

import tensorflow as tf


def l2_reg_cost(cost, model):
    """
        Calculates the cost of a neural network with L2 regularization
    """
    tensor = tf.stack(model.losses) + cost

    return tensor
