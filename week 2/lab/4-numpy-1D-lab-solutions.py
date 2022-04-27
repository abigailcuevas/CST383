# -*- coding: utf-8 -*-
"""
Lab for NumPy lecture 1 (solutions)

@author: Glenn
"""

import numpy as np

# problem 1: create a NumPy array x containing values 0 to 9
x = np.arange(10)

# problem 2: print array x
print(x)

# problem 3: write an expression to get the first three values in x.  Use slicing.
x[:3]

# problem 4: write an expression to get the last three values in x.  Use slicing.
x[-3:]

# problem 5: write an expression to get the first three values in x.  Use fancy indexing.
x[[0,1,2]]

# problem 6: create a NumPy array i containing 0,2,4,6,8.  Use np.arange
i = np.arange(0,9,2)

# problem 7: write an expression to index into x with array i.  Before running
# your answer, think of what you expect to get.
x[i]

# problem 8: write an expression to index into x with x itself.  Do you think
# you will get an error?  After you run your answer, explain what you got.
x[x]

# problem 9: create a NumPy array 'tuition' containing these tuition values for 8 colleges:
# 7440, 12280, 11250, 12960,  7560, 13500, 13290, 13868
tuition = np.array([7200, 12280, 11250, 12960,  7560, 13500, 13290, 13868])

# problem 10: write an expression to get the first 4 tuition values in tuition
tuition[:4]

# problem 11: I made a mistake.  The first tuition value should be 7440.
# Write an assignment statement to fix the tuition array.
tuition[0] = 7440

# problem 12: create a boolean array 'mask' that is the same length as tuition, and
# has value True whenever the corresponding value in tuition is below 10,000.
# Remember, the boolean values are True and False.
mask = np.array([True, False, False, False, True, False, False, False])

# problem 13: using mask, write an expression to get the tuition values that
# are below 10,000 from the tuition array.
tuition[mask]

# problem 14: repeat problem 13, but this time, instead of using array Mask,
# use a plain Python list containing boolean values.
tuition[[True, False, False, False, True, False, False, False]]

# problem 15: write an expression to index into array mask using array mask.
# Before running it, think about what you expect to get.  An error?
mask[mask]

# problem 15: write an expression to index into array x (that you defined
# earlier) with mask.  What do you expect to get?
x[mask]

# problem 16: What is the output of the following expression?
# Think about it before you run it.
np.array([1,3,5,7,9])[True, False, False, True, False]

# problem 17: What is the output of the following expression?
# Think about it before you run it.
np.array([1, 3, 5, 9])[[False, True, False, True]][[1, 0]]
