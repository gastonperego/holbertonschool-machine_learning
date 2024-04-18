#!/usr/bin/env python3
"""
    Task 6
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
        Generates a bar graph with the fruits owned by each person
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))
    names = ['Farrah', 'Fred', 'Felicia']

    print(fruit)
    print(fruit[0])

    plt.bar(names, fruit[0], color='r', label='apples', width=0.5)
    plt.bar(names, fruit[1], color='y',
            label='bananas', width=0.5, bottom=fruit[0])
    plt.bar(names, fruit[2], color='#ff8000',
            label='oranges', width=0.5, bottom=fruit[0] + fruit[1])
    plt.bar(names, fruit[3], color='#ffe5b4',
            label='peaches', width=0.5, bottom=fruit[0] + fruit[1] + fruit[2])
    plt.legend()
    plt.title('Number of Fruit per Person')
    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.show()
