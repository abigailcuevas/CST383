# -*- coding: utf-8 -*-
"""
Lab for NumPy lecture 2 (solutions)

@author: Glenn
"""

import numpy as np

# problem 1: write a statement to create a NumPy array x containing 
# values 'a', 'b', 'c', 'd'
x = np.array(['a','b','c','d'])

# problem 2: write an expression to get the type of the values in x
x.dtype

# problem 3: write an expression to get the first and third values in x.
# Use fancy indexing.
x[[0,2]]

# problem 4: write an expression to get the last three values in x.  Use slicing.
x[-3:]

# problem 5: create a NumPy arrax x containing 10 values between 0 and 20.
# hint: do not use np.arange()
x = np.linspace(0, 20, num=10)

# problem 6: print array x
print(x)

# problem 7: write an expression to get the type of x
x.dtype

# problem 8: print array x, but only show 2 digits after the decimal point
# hint: use np.round()
print(np.round(x, 2))

# problem 9: write an expression to get the average value of x
np.mean(x)

# problem 10: write an expression to get the values of array x, but
# with every value multiplied by 10.
x * 10

# problem 11: write a statement to create a NumPy array 'tuition' containing 
# these tuition values for 8 colleges:
# 7200, 12280, 11250, 12960,  7560, 13500, 13290, 13868
tuition = np.array([7200, 12280, 11250, 12960,  7560, 13500, 13290, 13868])

# problem 12: write an expression that will give a boolean array of the same length
# as tuition, and has value True whenever the corresponding value in 
# tuition is above 12,000.
tuition > 12000

# problem 13: repeat the previous problem, but this time assign the boolean array to 
# variable 'mask'
mask = tuition > 12000

# problem 14: using mask, write an expression to get the tuition values that
# are above 12,000 from the tuition array.
tuition[mask]

# problem 14: using mask, write an expression to get the tuition values that
# are less than or equal to 12,000 from the tuition array
tuition[~mask]

# problem 15: write an single expression to get the tuition values that are
# above 12,000, but use only variable tuition in your answer.
# Hint: you don't need the boolean mask to be stored as a variable
tuition[tuition > 12000]

# problem 16: write a statement to create a NumPy array 'private' containing
# these values:
# False, True, True, True, False, False, False, True, True, True
private = np.array([False, True, True, True, False, False, False, True])
    
# problem 17: if an item in array 'private' is True, the corresponding
# value in array tuition is for a private college.
# Write an expression to get the values in tuition that are for private
# colleges.
tuition[private]

# problem 18: write an expression to get the average tuition of
# private colleges
np.mean(tuition[private])

# problem 19: write an expression to get the minimum tuition of
# public (non-private) colleges
np.min(tuition[~private])

# problem 20: write an expression to find the colleges that
# are private and have tuition < 10,000.  Your answer should be a
# boolean array of the same length as tuition.
private & (tuition < 13000)
