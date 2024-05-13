#!/usr/bin/env python3
"""
    Create train op function
"""

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes,
          activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    """
        Builds, trains, and saves a neural network classifier:
    """
    a = 0
    sess = tf.Session()
    x, y = create_placeholders(len(X_train[0]), len(Y_train[0]))
    y_pred = forward_prop(x, layer_sizes, activations)
    acc = calculate_accuracy(y, y_pred)
    loss = calculate_loss(y, y_pred)
    train_op = create_train_op(loss, alpha)
    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init)
    for i in range(iterations + 1):
        if i == a:
            t_loss = sess.run(loss, feed_dict={x: X_train, y: Y_train})
            t_acc = sess.run(acc, feed_dict={x: X_train, y: Y_train})
            v_loss = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})
            v_acc = sess.run(acc, feed_dict={x: X_valid, y: Y_valid})
            print(f"After {i} iterations:")
            print(f"\tTraining Cost: {t_loss}")
            print(f"\tTraining Accuracy: {t_acc}")
            print(f"\tValidation Cost: {v_loss}")
            print(f"\tValidation Accuracy: {v_acc}")
        if i < iterations:
            sess.run(train_op, feed_dict={x: X_train, y: Y_train})
        a += 100

    saver = tf.train.Saver()
    s = saver.save(sess, save_path)

    return s
