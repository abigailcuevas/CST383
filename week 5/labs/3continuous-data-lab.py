# -*- coding: utf-8 -*-
"""
Continuous data lab.

Insert your code after the prompts.

@author: Dr. Bruns
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the very useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
#sns.set_context('paper')   # 'talk' for slightly larger
sns.set_context('talk')   # 'talk' for slightly larger

# change default plot size
rcParams['figure.figsize'] = 7,5

# read the penguins data
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
# remove rows containing NA values
df.dropna(inplace=True)

# preliminary exploration
df.info()

# first rows
df.head()

# basic statistics for the quantitative variables
df.describe()

# Do heavier penguins have longer bills?
# Make a scatter plot with bill length on x and weight on y.
# Use kilograms for weight instead of grams.
# Put a title and x and y axis labels on plot.
plt.scatter(df['bill_length_mm'], df['body_mass_g'])
plt.title('Penguin weight by billl length')
plt.xlabel('Bill length')
plt.ylabel('Weight (kg)')
# Histograms
#

# Plot a histogram of body mass using matplotlib.
# Give the plot a title and x and y axis labels.
plt.hist(df['body_mass_g'])
plt.title('Penguin weight by bill length')
plt.xlabel('Bill length')
plt.ylabel('Weight (kg)')

# Plot the same histogram, but this time use only 6 bars.
# (see matplotlib documentation for hist())

plt.hist(df['body_mass_g'], bins = 6)
plt.title('Penguin weight by bill length')
plt.xlabel('Bill Length')
plt.ylabel('Weight (kg)')

# Plot the same histogram again, but this time make is so
# that the bins are for every 500 g.  For example, the first
# bin should be from 2500-3000 grams, the next from 3000-3500 grams,
# etc.
plt.hist(df['body_mass_g'], bins = 6)
plt.title('Penguin weight by bill length')
plt.xlabel('Bill length')
plt.ylabel('Weight (kg)')


# Try again but this time make the bins 100 grams in width.


# Which is better, 100 or 500?


#
# single variable probabilities
#

# Estimate the probability that body mass is greater than 5000 g?
print((df['body_mass_g'] > 5000).mean())

# Estimate the probability that the body mass is between 4000 and 5000 g
print((df['body_mass_g'] > 4000 & df['body_mass_g'] < 5000 ).mean())

# Estimate the probability that the body mass is more than 20% below average?
# hint: first calculate the average, then multiply it by 0.8
average = df['body_mass_g'].mean() * 0.8
(df['body_mass_g'] > average) 

#
# joint probabilaties
#

# Look back at your scatter plot.  Some penguins are light but have
# long bills.  What's the probability of bill length greater than 50
# but body mass < 4.0 kg?
(df['bill_length_mm'] > )


# What is the probability that the body mass is greater than
# 4000 g and the penguin is a female?


# What is the probability that the body mass is greater than
# 4000 g and the penguin is a male?


#
# conditional probability
#

# what is the probability that the body mass is greater than
# 4000 g *given* the penguin is a male?


# what is the probability that the body mass is greater than
# 4000 g *given* the penguin is a female?


#
# density plot
#

# Create a density plot of body mass


# Create a density plot of body mass for female penguins


# the density plot for females is "bi-model": it is two bumps.
# Why do you think it might be bi-modal?
# Hint: this is a sign there might be two sub-populations.

# Create a single density plot of body mass containing two
# lines; one for males and one for females.
# Give your plot a legend to show the sex for each line.


