#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 00:08:10 2021

@author: vishakha

"""
import numpy as np


def monte_carlo(func,a=0,b=1,n=1000):
    subsets=np.arange(0,n+1,n/10)
    steps=n/10
    u=np.zeros(n)
    for i in range(10):
        start=int(subsets[i])
        end=int(subsets[i+1])
        u[start:end]=np.random.uniform(low=i, high=(i+1)/10, size=end-start)
    np.random.shuffle(u)
    
    u=np.random.uniform(size=n)
    u_func=func(a+(b-a)*u)
    s=((b-a)/n)*u_func.sum()
    
    return s

def f1(x):
    return (15*x**3+21*x**2+41*x+3)**(1/2)*(np.exp(-0.5*x))

integral=monte_carlo(f1, a=0, b=4, n=1000)
print(integral)
    
        