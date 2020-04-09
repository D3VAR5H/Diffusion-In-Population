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
    K = 11600000000
    A = 0.896974652
    E_k = 0.973026503

    # Error term
    # 17401081.969697*t  - 77506700.866667
    # 14840982.991667*t - 58732641.694444
    # (6354017.641667*t) - 26184928.416667
    time = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    file.write('[')
    for i in range(len(time)):
        t = time[i]
        Pt = int((K / (1 + (A * (E_k ** t)))) + ((6354017.641667 * t) - 26184928.416667))
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
    actual_population = [6.115, 6.274, 6.432, 6.594, 6.758, 6.923, 7.087, 7.256,
                         7.426, 7.594, 7.8]

    #  Fetch the generated data from file
    file = open(direc, 'r')
    data = file.read()

    # Remove the unusual data from file
    Estimated_population = data.split(',')
    Estimated_population[0] = Estimated_population[0].split('[')[1]
    Estimated_population.pop()

    # Generate the x and y coordinates for Graph
    error = []
    for i in range(len(Estimated_population)):
        Estimated_population[i] = int(Estimated_population[i]) / 1000000000
        error.append(
            int((Estimated_population[i] - actual_population[i]) * (10 ** 9)))

    print("Estimated Population")
    print(Estimated_population)
    print("Error In Calculations :")
    print(error)

    x = np.arange(len(time))  # the label locations
    width = 0.4  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, actual_population, width,
                    label='Actual Population ')
    rects2 = ax.bar(x + width / 2, Estimated_population, width,
                    label='Estimated Population')
    ax.set_ylabel('Population in billions(bn)')
    ax.set_xlabel('Year')
    ax.set_title('World Population')
    ax.set_ybound(lower=6.0, upper=8.0)
    ax.set_xticks(x)
    ax.set_xticklabels(time)
    ax.legend()

    fig.tight_layout()
    plt.show()

#  CITATION
# https://data.worldbank.org/indicator/SP.POP.TOTL?contextual=default&end=2018&locations=IN&start=2007&view=chart
