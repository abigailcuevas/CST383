# -*- coding: utf-8 -*-
"""
Lab for NumPy lecture 3 (solutions)

@author: Dr. Bruns
"""

import numpy as np
import pandas as pd

# Make a 2D Numpy array from 5 columns of the college data; 10 random rows
# Each row of X represents one college.
np.random.seed(3)
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)
X = df.sample(10)[['Apps', 'Accept', 'F.Undergrad', 'Outstate']].values

# problem 1: write a statement to print the shape of array X
print(X.shape)

# problem 2: write an expression to get the number of rows in X
# hint: X.shape is a Python tuple
X.shape[0]

# problem 3: write an expression to get the type of X
X.dtype

# problem 4: The first column of X gives the number of applications the
# college received in the year the dataset was collected.  Write a
# statement to assign the first column of X to variable 'apps'.
apps = X[:,0]

# problem 5: The second column is the number of applicants who were 
# accepted.  Write a statement to assign the second column of X to
# variable 'accept'.
accept = X[:,1]

# problem 6: A college is selective if only a small fraction of the
# applicants are accepted.  Write an expression to get the number
# of accepted divided by the number of applicants for the college
# on the first row of X.
X[0,1]/X[0,0]

# problem 7: Write an expression to get the number of accepted 
# divided by the number of applicants for all colleges in X.
# Your answer should be an array of length 10.  Don't use a loop!
X[:,1]/X[:,0]

# problem 8: The fourth column of X is out-of-state tuition.
# Write an expression to get the average out-of-state tuition in X.
# Hint: the numpy function for mean value is np.mean().
X[:,3].mean()

# problem 9: Write an expression to get the mean value for each
# of the four columns in X.
# Hint: the name of the function you need starts with "apply".
np.apply_along_axis(np.mean, 0, X)

# problem 10: Write an expression to get the median value for
# each column.
np.apply_along_axis(np.median, 0, X)

# problem 11: Write an expression to get the third row of X
X[2]

# problem 12: Write an expression to get the fourth column
# of the last two rows of X.  Use slicing.
X[-2:, 3]

# problem 13: Write an expression to get rows 1,3, and 7 of X.
# Use fancy indexing.
X[[1,3,7]]

# problem 14: Which values in x are below 1000?  Write an expression
# to get a boolean mask that is True for these values.
X < 1000

# problem 15: Repeat the previous problem, but this time write
# a statement that assigns the boolean mask to variable 'mask'.
mask = X < 1000

# problem 16: Write an expression to get the shape of variable mask.
# (How does it differ from the shape of X?)
mask.shape

# problem 17: Write an expression to get all the values in array
# X that are less than 1000.
X[mask]

# problem 18: The value in the third column is the number of full time
# undergraduates.  What is the average value in that column?
X[:,2].mean()

# problem 19: Write an expression to get the colleges for which
# the number of full-time undergraduates is below average.
# (In other words, get certain rows from X)
X[X[:,2] < X[:,2].mean()]

# problem 20: (A harder problem) Write an expression to get the average 
# out-of-state tuition (column 3) for colleges in which the
# number of full-time undergraduates (column 2).
# ("column 0" is the first column)
X[X[:,2] < X[:,2].mean()][:,3].mean()
