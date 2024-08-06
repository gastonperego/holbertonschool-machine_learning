#!/usr/bin/env python3
"""
    all_in_one: Plots 5 different graphs in one figure
"""
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """
        Plots a line graph on top left, a scatter graph on top right
        2 more line graphs below the first two and below that a histogram that
        occupates the whole widht of the image
    """
    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    
    fig = plt.figure(figsize=(6.4, 5.6))

    plt.subplot(3, 2, 1)
    plt.plot(y0, 'r')
    plt.xlim((0, 10))
    plt.yticks([0, 500, 1000])

    plt.subplot(3, 2, 2)
    plt.scatter(x1, y1, c='m')
    plt.xlabel('Height (in)', size='small')
    plt.ylabel('Weight (lbs)', size='small')
    plt.title('Men\'s Height vs Weight', size='small')

    plt.subplot(3, 2, 3)
    plt.plot(x2, y2)
    plt.xlabel('Time (years)', size='small')
    plt.ylabel('Fraction Remaining', size='small')
    plt.title('Exponential Decay of C-14', size='small')
    plt.xlim((0, 28650))
    plt.yscale('log')

    plt.subplot(3, 2, 4)
    plt.plot(x3, y31, 'r--', label='C-14')
    plt.plot(x3, y32, 'g-', label='Ra-226')
    plt.title('Exponential Decay of Radioactive Elements', size='small')
    plt.xlabel('Time (years)', size='small')
    plt.ylabel('Fraction Remaining', size='small')
    plt.xlim((0, 20000))
    plt.ylim((0, 1))
    plt.legend()

    plt.subplot2grid((3, 2), (2, 0), colspan=2)
    bins = np.arange(0, 101, 10)
    plt.hist(student_grades, bins, edgecolor='black')
    plt.xlabel('Grades', size='small')
    plt.ylabel('Number of Students', size='small')
    plt.title('Project A', size='small')
    plt.xticks(bins)
    plt.yticks([0, 10, 20, 30])
    plt.ylim((0, 30))
    plt.xlim((0, 100))

    fig.suptitle('All in One')
    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()
