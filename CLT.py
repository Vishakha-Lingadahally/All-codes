#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:54:59 2021

@author: vishakha
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from wand.image import Image
from wand.display import display

#Simulating 1000 die rolls
n=1000


#In each of the simulations, there happens to be one more trial than the previous one.
avg=[]
for i in range(2,n):
    a=np.random.randint(1,7,i)
    avg.append(np.average(a))


#Plotting histogram, where present is the latest figure
def clt(present):
    #It's time to stop if the animation is at the last frame.
    plt.cla()
    if present == 1000:
        a.event_source.stop()
        
    plt.hist(avg[0:present])
    
    plt.gca().set_title('Expected value of die rolls')
    plt.gca().set_xlabel('Average from die roll')
    plt.gca().set_ylabel('Frequency')
    
    plt.annotate('Die roll={}'.format(present), [3,27])
    
fig = plt.figure()
a = animation.FuncAnimation(fig, clt, interval=1)
#Save the figure at the destination of choice
a = a.save('/home/vishakha/Documents/python/clt.gif', writer='imagemagick', fps=10)