#!/usr/bin/python

import numpy as np
from pylab import *
import matplotlib.pyplot as plt

def de_mean(x):
	xmean = mean(x)
	return [xi - xmean for xi in x]

def covariance(x,y):
	n = len(x)
	return dot(de_mean(x), de_mean(y)) / (n - 1)

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0,10.0,1000)

scatter(pageSpeeds, purchaseAmount)
plt.show()

covariance(pageSpeeds, purchaseAmount)

purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)
plt.show()

covariance (pageSpeeds, purchaseAmount)

def correlation(x,y):
	stddevx = x.std()
	stddevy = y.std()
	return covariance(x,y) / stddevx / stddevy

print(correlation(pageSpeeds, purchaseAmount))


np.corrcoef(pageSpeeds, purchaseAmount)

# test
#x = np.array([2,3,4])
#print(100 + x)

purchaseAmount = 100 - pageSpeeds * 3

scatter(pageSpeeds, purchaseAmount)
plt.show()

print(correlation(pageSpeeds, purchaseAmount))