#!/usr/bin/env python3

import numpy as np
import tensorflow
tf = tensorflow.compat.v1
tf.disable_eager_execution()


def create_placeholders(nx, classes):
    """
        Returns two placeholders, x and y, for the neural network
    """
    x = tf.placeholder(tf.float32, [None, nx], name='x')
    y = tf.placeholder(tf.float32, [None, classes], name='y')

    return x, y
