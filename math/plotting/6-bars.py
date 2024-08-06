#!/usr/bin/env python3
"""
    bars: Plots a bar graph
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
        Plots a bar graph that contains the numer of fruits that each person
        has
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    plt.ylabel('Quantity of Fruit')
    plt.ylim((0, 80))
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80])
    plt.suptitle('Number of Fruit per Person')

    plt.bar(['Farrah', 'Fred', 'Felicia'], fruit[0], color='r',
            label='apples', width=0.5)
    plt.bar(['Farrah', 'Fred', 'Felicia'], fruit[1], bottom=fruit[0],
            color='y', label='bananas', width=0.5)
    plt.bar(['Farrah', 'Fred', 'Felicia'], fruit[2], bottom=fruit[0]
            + fruit[1], color='#ff8000', label='oranges', width=0.5)
    plt.bar(['Farrah', 'Fred', 'Felicia'], fruit[3], bottom=fruit[0]
            + fruit[1] + fruit[2], color='#ffe5b4', label='peaches', width=0.5)
    plt.legend()
    plt.savefig('plot.png')
    plt.show()
