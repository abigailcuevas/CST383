# -*- coding: utf-8 -*-
"""
Pandas dataframes lab

@author: Glenn Bruns
"""

import numpy as np
import pandas as pd

# here are the names of seven CSUMB students
students = ['Sean', 'Laura', 'Angel', 'Mariana', 'Austin', 'Jose', 'Ana']

# here are the MPG values for the students' cars
student_mileage = [21.1, 26.6, 16.3, 33.7, 31.2, 52.0, 27.1]

# here are the round-trip distances for the students' commutes to CSUMB
student_dist = [8.1, 5.4, 12.8, 15.0, 22.2, 18.5, 3.4]

# problem 1
# create a Pandas dataframe df containing a column 'mpg' and a
# column 'distance'.  The 'mpg' column should be first.
# The dataframe won't contain the student's names.
# YOUR CODE HERE
df = pd.DataFrame({'mpg' : student_mileage, 'distance':student_dist});

# problem 2
# print the dataframe you just created
print(df)

# problem 3
# write an expression to get the values in the 'mpg' column
print(df['mpg'])

# problem 4
# print the first three rows of df
print(df[:3])

# problem 5
# print three random rows of df
print(df.sample(3))

# problem 6
# write an expression to get the average round-trip distance
df['distance'].mean()

# problem 7
# swap the order of the two columns
df = [['distance' , 'mpg']]

# problem 8
# print df again
print(df)

# problem 9
# change the name of the 'distance' column to 'dist'
df.columns = ['dist']

# problem 10
# assume the cost of gas is $5/gallon, and add a new column 'cost'
# that gives the cost of a single commute.
# Hint: miles divided by miles/gallon gives gallons.  


# problem 11
# print the rows for which the commute cost > $2  (use a boolean mask)


# problem 12
# make the student names the index of df
# hint: df.index is the index of df


# problem 13
# print the mileage for Ana's car using the .loc attribute


# problem 14
# print the rows of the dataframe where mpg > 30 (use a boolean mask)


# problem 15
# print the rows for Laura and Austin using .loc


# problem 16
# drop the column distance


# problem 17
# write an expression using .iloc and .loc


# problem 18
# print the underlying 2D numpy array for df
# (Hint: you use .index on a data frame to get the row index; how do
# you get the data?)


# If you still have time, find a feature of dataframes not covered
# in lecture, and try it out in lab.
