#!/usr/bin/env python3
"""
    Task 4
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
        Creates a hist graph based on students grades in a test
    """

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    bins = np.arange(0, 101, 10)
    plt.hist(student_grades, bins, edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.xlim(0, 100)
    plt.xticks(bins, bins)
    plt.ylim(0, 30)
    plt.show()
