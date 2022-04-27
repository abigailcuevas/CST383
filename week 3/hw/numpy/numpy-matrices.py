# -*- coding: utf-8 -*-
"""

Using NumPy 2D arrays.

In this homework you will write code to work with 2D NumPy data.  We will 
use the small and famous Iris dataset.

See https://archive.ics.uci.edu/ml/datasets/iris for information on the dataset.

Each problem is defined using special comment lines:
    
#@ problem     Lines that start like this give the problem ID.

##             Lines that start like this give the problem description.

#@ assume      Lines that start like this list the variables you can refer
               to in your code.
               
#@ assign      Lines like are used when your answer should be an assignment
               statement, and give the variable to assign to.

If a problem doesn't have a #@ assign line, then your answer should 
be an expression.

Provide your answer on the first blank line after the problem lines.

None of your answers should be print statements.

Please ask if anything is not clear!

@author: Glenn Bruns
"""

import numpy as np
import pandas as pd    # for loading data only!

# Load the data

# X is a 2D NumPy array 
# - every row of X is an Iris flower that was measured
# - each column is a different feature of an Iris
# col_names is a 1D NumPy array
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/iris.csv")
X = df.values
col_names = df.columns

# look at the column names
print(col_names)

# look at the first five rows of the data
print(X[:5])

#@ problem 1
## Write an expression that gives the petal width of the flower in
## the third row of X.  The pedal width column can be selected by number.  
## The result should be a single number.  Check that your output is correct
## by looking at array X.
#@ assume X

X[2][3]


#@ problem 2
## Write an expression that gives the last five rows of X.
## Use slicing.  The result should be a 2D NumPy array.
#@ assume X
X[-5:]


#@ problem 3
## Write an expression that gives the petal length for the flowers
## in the last five rows of X.  The result should be a 1D NumPy array.
## Use a number to select the petal length column.
#@ assume X
X[-5:,2]



#@ problem 4
## Write an expression that gives the sepal length and sepal width for the flowers
## in the first five rows of X.  The result should be a 2D NumPy array.
## Use slicing or fancy indexing to select the sepal length and sepal width columns.
#@ assume X
X[:5, [0,1]]

#@ problem 5
## Write an expression that the 5 smallest sepal_length values in X.
## Your result should be a 1D NumPy array, and the values should be
## ordered in increasing order.  Use NumPy function 'sort'.
#@ assume X
np.sort(X[:, 0])[:5]


#@ problem 6
## Write an expression that gives all the pedal width values in X.
## Use a boolean mask to select the petal width column.  The boolean
## mask must be created using the col_names variable and the name
## of the column you want.  The result should be a 2D NumPy array, not a 1D array!  
#@ assume X,col_names
X[:, col_names == 'petal_width']


#@ problem 7
## Write an expression that computes the minimum petal width value in X.
## Use a boolean mask to select the petal width column.  
## The result should be a single number.
#@ assume X,col_names
np.min(X[:, col_names == 'petal_width'])


#@ problem 8
## Write an expression that gives the values in the 'species' column
## of X.  Use a boolean mask to select the species column.  This time,
## your result should be a 1D array, not a 2D array!
#@ assume X,col_names
(X[:, col_names == 'species']).flatten()


#@ problem 9
## Write an expression that gives the rows of X in which
## the value in the species column is 'virginica'.  Use a number
## to select the species column, but use a boolean mask to select
## the rows of X.  The result should be a 2D NumPy array.
#@ assume X
X[np.where(X[:,4] == 'virginica')] 


#@ problem 10
## Write an expression that gives gives all the petal_length values 
## in X for irises of species 'setosa'.  Use a boolean mask for both
## rows and columns.  The result should be a 1D NumPy array.
#@ assume X,col_names  
X[:, col_names == 'petal_length'][X[:,col_names == 'species'] == 'setosa'] 

#@ problem 11
## Write an expression that gives gives the average petal length
## of irises of species setosa. Use two boolean masks
## and the NumPy mean() function.  The result should be a number.
#@ assume X,col_names
(X[:, col_names == 'petal_length'][X[:,col_names == 'species'] == 'setosa' ]).mean()


