#!/usr/bin/env python3
"""
    Plots a histogram
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
        Plots a histogram of students scores for a project
    """

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    bins = np.arange(0, 101, 10)
    plt.hist(student_grades, bins, edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.xticks(bins)
    plt.ylim((0, 30))
    plt.xlim((0, 100))
    plt.savefig('plot.png')
    plt.show()
