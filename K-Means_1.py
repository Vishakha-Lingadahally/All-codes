#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 02:26:30 2021

@author: vishakha
"""
# Generate some data
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

X, y_true = make_blobs(n_samples=400, centers=6,
                       cluster_std=0.60, random_state=0)
X = X[:, ::-1] # flip axes for better plotting
plt.scatter(X[:,0],X[:,1])
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(4, random_state=0)
labels = kmeans.fit(X).predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis');