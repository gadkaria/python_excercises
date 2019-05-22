#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the important libraries
import pandas as pd

import numpy as np


# In[2]:


# load data of all footballers in fifa18 
fifa_data = pd.read_csv("https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv")


# In[3]:


# check to see if load is sucessfull
print(fifa_data.head())


# In[30]:


# find all players who are young with high potential
prospects = fifa_data.loc[(fifa_data['Age'] < 23) & (fifa_data['Potential'] > 85)]


# In[25]:


# all highly rated United States youngsters
US_hyped_players = prospects.loc[prospects['Nationality'] == 'United States']


# In[26]:


US_hyped_players.set_index('Potential', inplace = True)


# In[27]:


#print(US_hyped)


# In[33]:


# Kylian Mbappe data 
prospects[prospects['Name'] == 'K. Mbappé']


# In[55]:


# players who are younger than 23 and have more than 85 in potential
young_strikers = fifa_data.loc[(fifa_data['Age'] < 23) & (fifa_data['Potential'] > 85)]

# filters the pool farther with players either having a high finishing or a high sprint speed
# as both are important in the game
young_strikers[(young_strikers['Finishing'] > 70) | (young_strikers['SprintSpeed'] > 75)] 

#removes all the unnecessary columns and data
young_str = young_strikers[['Name','Age','Value', 'Potential', 'Club', 'SprintSpeed']]

# sort data by Age of players, with the youngest at the top
young_str.sort_values(by=['Age'], ascending=True)


# In[ ]:




