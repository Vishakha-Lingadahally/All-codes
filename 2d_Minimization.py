#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 01:02:03 2021

@author: vishakha
"""
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function that we are interested in
def f(x):
    return ((np.sin(x[0]))*(np.cos(x[1])))

# Make a grid to evaluate the function (for plotting)
x = np.linspace(-2, 2)
y = np.linspace(-1, 1)
xg, yg = np.meshgrid(x, y)


plt.figure()
plt.imshow(f([xg, yg]), extent=[-2, 2, -1, 1], origin="lower")
plt.colorbar()
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xg, yg, f([xg, yg]), rstride=1, cstride=1,
                       cmap=plt.cm.jet, linewidth=0, antialiased=False)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('3D plot of f(x)')

#Minimization
x_min = optimize.minimize(f, x0=[0,0])
print(x_min)

# Show the function in 2D
plt.figure()
plt.imshow(f([xg, yg]), extent=[-2, 2, -2, 2], origin="lower")
plt.colorbar()

# And the minimum to the plot
plt.scatter(x_min.x[0], x_min.x[1])

plt.show()
