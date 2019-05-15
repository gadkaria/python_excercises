#!/usr/bin/env python3
# coding: utf-8

# step 1: Clean the data, normalize params and give numerical values to non numerical attributes

# step 2: Choose k random centriods

# step 3: find the distance of each data point to each centriod

# step 4: re-calculate centriod 

# step 5: stop iterating once difference between old and new centriod is neglible

import pandas as pd

import numpy as np

import math

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# import data        
url = "https://raw.githubusercontent.com/madhug-nadig/Machine-Learning-Algorithms-from-Scratch/master/data/ipl.csv"
data = pd.read_csv(url)
X = data.values  


class Kmeans:
    def __init__(self, k = 2, tol = 0.0001, max_iter = 500):
        self.k_value = k
        self.tolerance = tol
        self.max_iterations = max_iter
    
    def cluster(self, data):
        
        # create dictionary of centriods 
        self.centroids = {}
        
        # pick first k centroids at random
        for i in range(self.k_value):
            self.centroids[i] = data[i]
        
        # start iterating till max_iterations 
        for i in range(self.max_iterations):
            self.classes = {}
            
            # clear classes
            for i in range(self.k_value):
                self.classes[i] = []

            for features in data:
                # calculating the distance of each point to the each centroid
                distances = [np.linalg.norm(features - self.centroids[centroid]) for centroid in self.centroids] 
                
                # finding the closest centroid
                close_centroid = distances.index(min(distances))
                
                # add this data point to the classes 
                self.classes[close_centroid].append(features)
                
            #recalculate the centroids
            
            prev_cent = dict(self.centroids)
            
            
            for cent in self.classes:
                self.centroids[cent] = np.average(self.classes[cent], axis = 0)
            
            # bool
            isDone = True
            
            # check to see if there is a neglibile difference 
            
            for cent in self.centroids:
                if np.sum((prev_cent[cent] - self.centroids[cent])/self.centroids[cent] * 100)  > self.tolerance:
                    isDone = False
            
            if isDone:
                break
                
        


# In[23]:


k = Kmeans(3)
k.cluster(X)


colors = 10*["r", "g", "c", "b", "k"]

for centroid in k.centroids:
    plt.scatter(k.centroids[centroid][0], k.centroids[centroid][1], s = 130, marker = "x")

for classification in k.classes:
    color = colors[classification]
    for features in k.classes[classification]:
        plt.scatter(features[0], features[1], color = color,s = 30)

plt.show()







