# -*- coding: utf-8 -*-
"""

Hyperparameter tuning lab

"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, ParameterGrid, GridSearchCV, RandomizedSearchCV

sns.set()
sns.set_context('notebook')   # larger
# default plot size
rcParams['figure.figsize'] = 8,6

#
# knn classification with college data
#

df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)

predictors = ['Outstate', 'F.Undergrad']
target = 'Private'
X = df[predictors].values			    
y = (df['Private'] == 'Yes').values.astype(int) # Private = 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#
# Problem 1: grid search
#

grid = [ {'n_neighbors': range(3,22,2), 'weights': ['uniform', 'distance'], 'p': [1,2]} ]    
# YOUR CODE HERE: define the grid

best_acc = 0
best_params = None
for params in ParameterGrid(grid):
    clf = KNeighborsClassifier(n_neighbors=params['k'],
                               weights=params['weights'],
                               p=params['p'])
    clf.fit(X_train, y_train)
    test_acc = clf.score(X_test, y_test)
    if test_acc > best_acc:
        best_acc = test_acc
        best_params = params
    print(params)
    
print("Best accuracy: {:.2f}".format(best_acc))
print("Best params: {}".format(best_params))
        
#
# Problem 2: grid search with cross validation
#

# YOUR CODE HERE: write code to do the grid search with cross validation

#
# Problem 3: randomized grid search with cross validation
#

# YOUR CODE HERE: write code to do randomized grid search

#
# Problem 4: succesive halving  (if you have time)
#




