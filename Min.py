#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 00:05:43 2021

@author: vishakha
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize



def f(x):
    return np.sin(x)



# The default (Nelder Mead)
print(optimize.minimize(f, x0=0))

x = np.arange(-10, 100, 0.1)
plt.plot(x, f(x))
#plt.annotate("Minimum", (0,optimize.minimize(f,x0=0)))
plt.show()


