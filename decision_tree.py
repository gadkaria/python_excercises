#!/usr/bin/env python
# coding: utf-8


# import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import pandas as pd
import numpy as np

#import data

balance_data = pd.read_csv('C:\\Users\\ameya\\Downloads\\balance-scale.data', sep= ',', header= None)
print(len(balance_data))
print(balance_data.shape)


# print first 5 rows of data
balance_data[0:5]



# split test and train data
X = balance_data.values[:,1:5]
Y = balance_data.values[:,0]

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

#create DecisionTree
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=3, min_samples_leaf=5)

# training the tree
clf_gini.fit(X_train, Y_train)

# creating and training the tree, except this is with entropy as the quality of the split
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, Y_train)

# now we test our models and check the accuracy

clf_gini.predict([[4, 4, 3, 3]])


# now have it predict against the test array

pred = clf_gini.predict(X_test)


# predict using the entropy tree

pred_en = clf_entropy.predict(X_test)

#print accuracy scores
print('Accuracy score for gini is', accuracy_score(Y_test,pred)*100)
print('Accuracy score for en is', accuracy_score(Y_test, pred_en)*100)





