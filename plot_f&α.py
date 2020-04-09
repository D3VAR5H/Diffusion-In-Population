import matplotlib.pyplot as plt
import os
import math
import numpy
from scipy.interpolate import interp1d
from random import random
from pylab import *


def growth_term(direc):
    file = open(direc, 'w')

    # Ratios - growth rate
    ratio = [0.01, 0.1, 0.5, 0.875]

    # Birth and Death Probability
    # do is 0 for our IBM data.
    b = [1, 0.8, 0.5, 0.3, 0.1]
    do = 0
    # 1. Layer Start
    for item in range(len(b)):
        bo = b[item]
        file.write('[')

        # 2. Layer Start
        for i in range(len(ratio)):
            several_means = []
            theta = ratio[i] * bo
            alpha = ratio[i]
            f = (2 * alpha * (1 - theta)) / (2 - bo)
            file.write(str(f)[:7] + ', ')
        # 2. Layer End

        file.write(']\n')
    # 1. Layer End

    file.close()
    # return


if __name__ == "__main__":
    # Get the path for storing the data
    direc = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'data.txt')

    #  Calculate the growth term
    growth_term(direc)

    #  Fetch the generated data from file
    file = open(direc, 'r')
    data = file.read()

    # Remove the unusual data from file
    l = data.split(']')
    list1 = l[0].split(',')
    list2 = l[1].split(',')
    list3 = l[2].split(',')
    list4 = l[3].split(',')
    list5 = l[4].split(',')
    list1[0] = list1[0].split('[')[1]
    list2[0] = list2[0].split('[')[1]
    list3[0] = list3[0].split('[')[1]
    list4[0] = list4[0].split('[')[1]
    list5[0] = list5[0].split('[')[1]
    list1.pop()
    list2.pop()
    list3.pop()
    list4.pop()
    list5.pop()

    for i in range(len(list1)):
        list1[i] = float(list1[i])
        list2[i] = float(list2[i])
        list3[i] = float(list3[i])
        list4[i] = float(list4[i])
        list5[i] = float(list5[i])

    # Generate the x and y coordinates for Graph
    alpha = [0.01, 0.1, 0.5, 0.875]
    print(list1, '\n', list2, '\n', list3, '\n', list4, '\n', list5)

    # Convert the x coordinates to array
    x = numpy.array(alpha)
    x_new = np.linspace(x.min(), x.max(), 500)

    # Set the limit for Y-axis.
    plt.ylim([0.0, 1.0])

    # Plot the graph for 'bo = 1'.
    y = numpy.array(list1)
    f = interp1d(x, y, kind='quadratic')
    y_smooth = f(x_new)
    plt.plot(x_new, y_smooth, label="bo = 1", linestyle="dashed")
    plt.scatter(x, y)

    # Plot the graph for 'bo = 0.8'.
    y = numpy.array(list2)
    f = interp1d(x, y, kind='quadratic')
    y_smooth = f(x_new)
    plt.plot(x_new, y_smooth, label="bo = 0.8", linestyle="solid")
    plt.scatter(x, y)

    # Plot the graph for 'bo = 0.5'.
    y = numpy.array(list3)
    f = interp1d(x, y, kind='quadratic')
    y_smooth = f(x_new)
    plt.plot(x_new, y_smooth, label="bo = 0.5", linestyle="dotted")
    plt.scatter(x, y)

    # Plot the graph for 'bo = 0.3'.
    y = numpy.array(list4)
    f = interp1d(x, y, kind='quadratic')
    y_smooth = f(x_new)
    plt.plot(x_new, y_smooth, label="bo = 0.3", linestyle="dashdot")
    plt.scatter(x, y)

    # Plot the graph for 'bo = 0.1'.
    y = numpy.array(list5)
    f = interp1d(x, y, kind='quadratic')
    y_smooth = f(x_new)
    plt.plot(x_new, y_smooth, label="bo = 0.1", linestyle="dashed")
    plt.scatter(x, y)

    # Display the final plots with labels
    plt.xlabel('log(K)')
    plt.ylabel('<N>/K')
    plt.legend()
    plt.show()
