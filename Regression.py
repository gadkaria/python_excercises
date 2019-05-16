#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

import matplotlib.pyplot as plt

# set up the data
X = np.array([0,1,2,3,4,5,6,7,8,9])
Y = np.array([1,3,2,5,7,8,8,9,10,12])
 


# In[5]:


# calculate the bars 
x_mean = np.mean(X)
y_mean = np.mean(Y)


# In[7]:


# calculating cross-deviation and deviation about x 
n = np.size(X)
SS_xy = np.sum(X*Y) - n*x_mean*y_mean
SS_xx = np.sum(X*X) - n*x_mean*x_mean


b_1 = SS_xy / SS_xx
b_0 = y_mean - b_1*x_mean


# In[8]:


# plotting the actual points as scatter plot 
plt.scatter(X, Y, color = "m", marker = "o", s = 30) 
  
# predicted response vector 
y_pred = b_0 + b_1*X 
  
# plotting the regression line 
plt.plot(X, y_pred, color = "g") 
  
# putting labels 
plt.xlabel('x') 
plt.ylabel('y') 
  
# function to show plot 
plt.show() 


# In[ ]:




