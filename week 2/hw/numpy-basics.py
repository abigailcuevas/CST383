# -*- coding: utf-8 -*-

"""
NumPy basics

In this homework you will write Python and NumPy code.
Your work will be graded automatically, so please read these
instructions carefully.

Each problem is defined using special comment lines:
    
#@ problem     Lines that start like this give the problem ID.

##             Lines that start like this give the problem description.

#@ assume      Lines that start like this list the variables you can refer
               to in your code.
               
#@ assign      Lines like are used when your answer should be an assignment
               statement, and give the variable to assign to.

If a problem doesn't have a #@ line, then your answer should be an expression.

Provide your answer on the first blank line after the problem lines.

None of your answers should be print statements.

# Please ask if anything is not clear!

@author: Glenn Bruns
"""

import numpy as np

# In the problem below, the problem number is 1, you code is allowed
# to refer to variable z, and your answer should be an assignment to variable x.

#@ problem 1
## assign the value of variable z to variable x
#@ assume z
#@ assign x
# YOUR CODE GOES HERE  (and the same for each problem below)
x = z

#@ problem 2
## assign 'hello' to variable msg
#@ assign msg
msg = 'hello'

#@ problem 3 
## check whether variable msg is a string
## Example: if msg = 5.0, the result should be False.
#@ assume msg
isinstance(msg, str)

#@ problem 4
## write an expression to square x
## Example: if x is 2.5, the result should be 6.25
#@ assume x
x**2


#@ problem 5 
## compute the length of the string obtained by appending strings 
## s1 and s2, with a space between them
## Example: if s1 is 'foo', and s2 is 'bar', the result should be 7
#@ assume s1,s2
len(s1) + len(' ') + len(s2)


#@ problem 6
## compute the substring consisting of the 2nd-4th characters of string s
## Example: if s is 'snorkel', the result should be 'nor'.
#@ assume s
s[1:4]


#@ problem 7
## In one of the first lectures of class, we looked at creating a
## system to identify the part number of a transmission part, based on
## width and length measurements (the "features" of the part).  Here
## is data for some examples of three types of parts:
##
# part1: 3.1, 5.2
# part1: 3.0, 5.3
# part1: 3.0, 5.2
# part2: 3.1, 4.8
# part2: 3.2, 4.9
# part2: 3.2, 4.8
# part3: 3.4, 5.6
# part3: 3.4, 5.5
# part3: 3.3, 5.4
#
# Each row above represents 1 part. The first value in each row is the
# part number, the second value is the part width, and the
# third value is the part length (width and length are in inches).
# The width and length values for part 1 vary a little because
# of manufacturing and measuring variations.  Similarly for the other 
# parts.
#
# Create a NumPy array 'width' that contains the width values
# in the data, from top to bottom.  
# Example: width[8] should give 3.3 
#@ assign width
width = np.array([3.1, 3.0, 3.0, 3.1, 3.2, 3.2, 3.4, 3.4, 3.3 ])


#@ problem 8
## Repeat the previous problem, but create a NumPy array 'length'
## that contains the length values in the data.
#@ assign length
length = np.array([5.2, 5.3, 5.2, 4.8, 4.9, 4.8, 5.6, 5.5, 5.4])


#@ problem 9
## Compute a numpy array containing the square root of every element 
## in array 'length'.
## Do not use a loop.
## Example: the result should have 9 elements, and the last should be
## about 2.32
#@ assume length
np.sqrt(length)


#@ problem 10
## write an expression to compute the average value in the array 'width'
## You can assume 'width' is non-empty and numeric.
#@ assume width
np.mean(width)


#@ problem 11
## write an expression to check that arrays 'width' and 'length' have
## the same number of elements
#@ assume width,length
len(width) == len(length)


#@ problem 12
## write an expression to compute the maximum value in array 'length'
#@ assume length
np.max(length)

#@ problem 13
## create a NumPy array 'part_num' containing the part numbers in
## the data set shown above, from top to bottom.  
## Example: part_num[3] should be 'part2'. 
#@ assign part_num
part_num = np.array(['part1', 'part1', 'part1', 'part2', 'part2', 'part2','part3', 'part3', 'part3'])

#@ problem 14
## create a Boolean array 'mask' that, for each element in array 'width',
## is True if the value is greater than 3.15, else False. 
## Example: mask[8] should be True
#@ assume width
#@ assign mask
mask = width > 3.15

 
#@ problem 15
## using the variable 'mask' just defined, compute an array
## of the part numbers of the parts for which width is greater than 3.15
#@ assume mask
mask[width > 3.15]


#@ problem 16
## using 'mask' again, compute the fraction of values in mask
## that are True.  You code should work correctly as long as 'mask' 
## is a boolean array.
## Example: the result should be about 0.555 for the 'mask' array
## you defined above, because about 55% of values in array 'width'
## are greater than 3.15
#@ assume mask
mask.mean()
   

#@ problem 17
## write an expression that gives the values in array 'width'
## that correspond to the values in array 'length' that are
## less than 5.0.  Your code should work for any numeric
## arrays 'width' and 'length' that are the same size.
## Example: for the 'width' and 'length' arrays you defined
## your result should be 3.1, 3.2, 3.2
#@ assume width,length
width[length < 5.0]


#@ problem 18
## compute the mean-zeroed version of width by subtracting
## each element of 'width' from the average value of width.
## Do not use a loop, and do not modify 'width'.
## Example: for the 'width' array you defined, the result
## should have 9 elements and the first should be about -0.0889
#@ assume width
width - np.mean(width)


#@ problem 19
## compute a '0-1 scaled' version of array 'length' by subtracting
## the minimum value of length from each element, and then 
## dividing each element in the result by the difference between
## the maximum and minimum values of length.
## Your final result should have the same number of elements as
## 'length', and should have 0 as its min value and 1 as its max
## value.
## Do not use a loop, and do not modify 'length'.
#@ assume length
(length - np.min(length)) / ( np.max(length) - np.min(length))


#@ problem 20
## create a 1D NumPy array 'parts' that contains the 'width'
## values followed by the 'length' values.  
## Example: The first values of 'parts' should be 3.1, 3.0, 3.0 
## and the last values should be 3.4, 3.4, 3.3.
#@ assume width,length
#@ assign parts
parts = np.array([width] + [length])

