#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:06:59 2021

@author: vishakha
"""
import numpy
import matplotlib.pyplot as plt
  
# Number of samples
N = [1, 10, 50, 100]  
# List of sample means
means = []  
  
# Generating 1, 10, 30, 100 random numbers from -40 to 40 and taking their mean and appending it to list means.
for j in N:
    # Generating seed so that we can get the same result 
    # Every time the loop is run,
    numpy.random.seed(1)
    x = [numpy.mean(
        numpy.random.randint(
            -40, 40, j)) for _i in range(1000)]
    means.append(x)
k = 0
  
# Plotting all means in
fig, ax = plt.subplots(2, 2, figsize =(8, 8))
for i in range(0, 2):
    for j in range(0, 2):
        # Histogram for each x stored in means
        ax[i, j].hist(means[k], 10, density = True)
        ax[i, j].set_title(label = N[k])
        k = k + 1
        
# The plot shows how the distribution resembles Gaussian with increasing N