#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 01:21:45 2021

@author: vishakha
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read the data (mixture model)
data = pd.read_csv('K-means_data.csv')

# Plot the data
plt.figure(figsize=(7,7))
plt.scatter(data["Weight"],data["Height"])
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Mixture model-Data distribution')
plt.show()

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=4)
kmeans.fit(data)

# Implement K-means algorithm from sklearn 

prediction=kmeans.predict(data)
frame=pd.DataFrame(data)
frame['cluster']=prediction
frame.columns=['Weight', 'Height', 'cluster']

color=['blue','green','cyan', 'black']
for k in range (0,4):
    data=frame[frame['cluster']==k]
    plt.scatter(data['Weight'], data['Height'], c=color[k])
    plt.xlabel('Weight')
    plt.ylabel('Height')
    plt.title('K-Means implementation for the mixture model')
plt.show()