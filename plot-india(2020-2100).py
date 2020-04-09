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
    K = 2000000000
    A = 0.892907707
    E_k = 0.963666191

    # Error term
    # 1296656.084848 - 6637036.333333
    time = []
    for i in range(0, 9):
        time.append(i * 10 + 20)
    file.write('[')
    for i in range(len(time)):
        t = time[i]
        Pt = int(K / (1 + (A * (E_k ** t))) - ((1296656.084848 * t) - 6637036.333333))
        file.write(str(Pt) + ', ')

    file.write(']\n')
    file.close()
    # return


def autolabel(rects, xpos='center'):
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{0:.3f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos] * 3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


if __name__ == "__main__":

    # Get the path for storing the data
    direc = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'data.txt')

    #  Calculate the growth term
    growth_term(direc)

    # List of Years
    time = []
    for i in range(0, 9):
        time.append(i * 10 + 2020)

    #  Fetch the generated data from file
    file = open(direc, 'r')
    data = file.read()

    # Remove the unusual data from file
    Estimated_Population = data.split(',')
    Estimated_Population[0] = Estimated_Population[0].split('[')[1]
    Estimated_Population.pop()

    # Generate the x and y coordinates for Graph
    for i in range(len(time)):
        Estimated_Population[i] = int(Estimated_Population[i]) / 1000000000
    print("Calculated Population")
    print(Estimated_Population)

    x = np.arange(len(time))  # the label locations
    width = 0.75  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, Estimated_Population, width, label='Estimated Population ')
    ax.set_ylabel('Population in billions(bn)')
    ax.set_xlabel('Year')
    ax.set_title('Population in INDIA (2020-2100)')
    ax.set_ybound(lower=1.35, upper=1.95)
    ax.set_xticks(x)
    ax.set_xticklabels(time)
    ax.legend()
    autolabel(rects1)
    fig.tight_layout()
    plt.show()

#  CITATION
# https://www.macrotrends.net/countries/IND/india/population
# https://data.worldbank.org/indicator/SP.POP.TOTL?contextual=default&end=2018&locations=IN&start=2007&view=chart
