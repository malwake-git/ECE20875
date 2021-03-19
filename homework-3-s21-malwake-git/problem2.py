# importing packages
from helper import getData

import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

dataA = getData('distA.csv')

stats.probplot(dataA, dist = 'norm', plot=plt)
plt.show()

dataB = getData('distB.csv')

stats.probplot(dataB, dist = 'laplace', plot=plt)
plt.show()

dataC = getData('distC.csv')

stats.probplot(dataC, dist = 'expon', plot=plt)
plt.show()
