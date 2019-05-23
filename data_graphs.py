#!/usr/bin/env python
# coding: utf-8

# In[29]:


# import the important libraries
import pandas as pd

import numpy as np

#graphing libraries
import plotly.plotly as py
import plotly.graph_objs as go


# In[10]:


# load data of all footballers in fifa18 
fifa_data = pd.read_csv("https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv")


# In[11]:


# check to see if load is sucessfull
print(fifa_data.head())


# In[12]:


# find all players who are young with high potential
prospects = fifa_data.loc[(fifa_data['Age'] < 23) & (fifa_data['Potential'] > 85)]


# In[13]:


# all highly rated United States youngsters
US_hyped_players = prospects.loc[prospects['Nationality'] == 'United States']


# In[14]:


US_hyped_players.set_index('Potential', inplace = True)


# In[15]:


#print(US_hyped)


# In[16]:


# Kylian Mbappe data 
prospects[prospects['Name'] == 'K. Mbappé']


# In[17]:


# players who are younger than 23 and have more than 85 in potential
young_strikers = fifa_data.loc[(fifa_data['Age'] < 23) & (fifa_data['Potential'] > 85)]

# filters the pool farther with players either having a high finishing or a high sprint speed
# as both are important in the game
young_strikers[(young_strikers['Finishing'] > 70) | (young_strikers['SprintSpeed'] > 75)] 

#removes all the unnecessary columns and data
young_str = young_strikers[['Name','Age','Value', 'Potential', 'Club', 'SprintSpeed']]

# sort data by Age of players, with the youngest at the top
print(young_str.sort_values(by=['Age'], ascending=True))


# In[18]:


fifa_data.iloc[0,2]


# In[35]:


# number of nations
player_num = []
player_num.append(len(fifa_data[fifa_data['Nationality'] == 'France']))
player_num.append(len(fifa_data[fifa_data['Nationality'] == 'England']))
player_num.append(len(fifa_data[fifa_data['Nationality'] == 'Germany']))
player_num.append(len(fifa_data[fifa_data['Nationality'] == 'Spain']))
total = np.array(player_num)
total_big_4 = total.sum()
print(fifa_data[['Nationality']])
player_num.append(len(fifa_data[['Nationality']])-total_big_4)


# In[36]:


print(player_num)
print(total.sum())


# In[37]:


labels = ['France','England','Germany','Spain', 'Rest of the world']


# In[38]:


trace = go.Pie(labels=labels, values=player_num)

py.iplot([trace], filename='big_4player_distro')


# In[43]:


# Scatter plot of potential vs Age
data_x = fifa_data['Potential']
# print(data_x)
x = np.array(data_x)
y = np.array(fifa_data['Age'])
print(x)


# In[46]:


scatter = go.Scatter(x=y,y=x, mode = 'markers')


# In[48]:


py.iplot([scatter], filename = 'age vs potential')


# In[ ]:




