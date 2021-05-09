#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 00:55:44 2021

@author: vishakha
"""

import numpy as np
import scipy.stats
import scipy.stats as stats
import matplotlib.pyplot as plt
import sympy as s

s.init_printing()

x = s.symbols("x")
f = x * s.exp(-(x ** 2) / 2)
f.integrate(x)
f.integrate((x, 0, s.oo))
f.integrate((x, 0.32, 2.45))

fn = s.lambdify([x], f)

xs = np.linspace(0, 5, 100)
plt.plot(xs, fn(xs))
xs = np.linspace(0.32, 2.45, 50)
plt.fill_between(xs, fn(xs), color="C1", alpha=0.3)
plt.ylim(ymin=0)
plt.show()
