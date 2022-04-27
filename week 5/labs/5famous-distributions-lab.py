# -*- coding: utf-8 -*-
"""
Probability: Famous distributions

@author: Glenn
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import patches, rcParams
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from rejection_sampling import rejection_sample

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the very useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
# sns.set_context('paper')   # 'talk' for slightly larger
# sns.set_context('notebook')
sns.set_context('talk')   # 'talk' for slightly larger
sns.set_style('whitegrid')

# set default plot size
rcParams['figure.figsize'] = 6,4

# START OF LAB --------------------------------------------------------

# ----------------------------------------------------------------------
# Binomial distribution
# ----------------------------------------------------------------------

# The Dodgers win 70% of the games they play.  What is the
# probability that they will win all 3 games they play against
# the Giants?
# Use stats.binom to create a variable dodgers, then use pmf().
dodgers = stats.binom(3, 0.7);
print(dodgers)

# The Dodgers win 70% of the games they play.  On average, how
# many games will they win when they play 3 games? 
# Use your dodgers variable.



# Get the answer to the last problem by looking at the Wikipedia
# page for binomial distribution.  You only need to look at the
# column on the right near the top of the page.
# Make sure to discuss this with your teammates.


# If I flip a fair coin 100 times, what is the probability that
# I will get heads 70 times?  
# Use stats.binom.


# I have a binomial distribution in which the probability of success
# is 0.6 and the number of trials is 3.  What are the possible values
# of the distribution?


# For the binomial distribution of the last problem, use stats.binom
# to get the probability associated with each value.  Store the
# probabilities in a Pandas series.  The index of the series should
# be the values.  Plot the PMF of the distribution as a bar plot
# using Pandas.


# ----------------------------------------------------------------------
# Normal distribution (aka Gaussian distribution aka bell-shaped curve)
# ----------------------------------------------------------------------

# create a random variable 'maxhr' using stats.norm
# use 150 as the mean value, and 23 as the standard deviation


# plot the pdf of maxhr


# Estimate the standard deviation of maxhr by looking at the plot.
# Then, compute the standard deviation using maxhr.


# What do you get if you add 3 standard deviations to the mean of maxhr?
# After you compute the value, look at where the value is on your plot.


# What do you think is the probability that max heart rate is less
# than 100?  Make a guess by looking at the plot, then compute your
# answer using maxhr.  Use function cdf().  


# What do you think is the probability that max heart rate is greater
# than 175?  Make a guess by looking at the plot, then compute your
# answer using maxhr.  Use function cdf().  



