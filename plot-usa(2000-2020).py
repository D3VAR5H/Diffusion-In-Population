import matplotlib.pyplot as plt
import matplotlib
import os
import math
import numpy
from scipy.interpolate import interp1d
from random import random
from pylab import *


def growth_term(direc):
    file = open(direc, 'w')

    # Constant Terms :
    K = 534000000
    A = 0.89556024
    E_k = 0.97845448

    # Error term
    # (579102.814286*t) - 4805021.714286
    time = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    file.write('[')
    for i in range(len(time)):
        t = time[i]
        Pt = int((K / (1 + (A * (E_k ** t)))) - ((579102.814286*t) - 4805021.714286))
        file.write(str(Pt) + ', ')

    file.write(']\n')
    file.close()
    # return


if __name__ == "__main__":

    # Get the path for storing the data
    direc = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'data.txt')

    #  Calculate the growth term
    growth_term(direc)

    # Actual Population
    time = [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020]
    actual_population = [0.281710909, 0.287279318, 0.292354658, 0.297758969,
                         0.303486012, 0.309011475, 0.314043885, 0.318673411,
                         0.323015995, 0.327096265, 0.331002651]

    #  Fetch the generated data from file
    file = open(direc, 'r')
    data = file.read()

    # Remove the unusual data from file
    Estimated_population = data.split(',')
    Estimated_population[0] = Estimated_population[0].split('[')[1]
    Estimated_population.pop()

    # Generate the x and y coordinates for Graph
    error = []
    for i in range(len(time)):
        Estimated_population[i] = int(Estimated_population[i]) / 1000000000
        error.append(int((Estimated_population[i] - actual_population[i]) * (10 ** 9)))
    print("Estimated Population")
    print(Estimated_population)
    print("Error In Calculations :")
    print(error)

    x = np.arange(len(time))  # the label locations
    width = 0.4  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, actual_population, width, label='Actual Population ')
    rects2 = ax.bar(x + width / 2, Estimated_population, width,
                    label='Estimated Population')
    ax.set_ylabel('Population in billions(bn)')
    ax.set_xlabel('Year')
    ax.set_title('Population of USA')
    ax.set_ybound(lower=0.2, upper=0.4)
    ax.set_xticks(x)
    ax.set_xticklabels(time)
    ax.legend()

    fig.tight_layout()
    plt.show()

#  CITATION
# https://data.worldbank.org/indicator/SP.POP.TOTL?contextual=default&end=2018&locations=IN&start=2007&view=chart
