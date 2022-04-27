# -*- coding: utf-8 -*-
"""
Correlation: South Park data

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

#
# read data
# 
# number of words spoken by each character in every episode of the TV series South Park
#

df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/south-park-word-counts.csv')

df.info()

df.head()

#@ 1
# for each character, compute the average number of words spoken per episode
# (don't use a loop; you only need about 10 character total)
print(df.mean())

#@ 2
# create an array of character names, sorted by the average number of words they speak
# per episode.  Call it 'top_characters'.
top_characters = np.array(df.sum().sort_values(ascending= False).index)
print(top_characters)
#@ 3
# Create a histogram of words per episode for Cartman
plt.hist(df['Cartman'])
plt.title('Histogram of word per episode from Cartman')


#@ 4
# how do number of words spoken by Cartman and Stan relate?
# Create a scatterplot showing words/episode for Cartman (x axis) and Stan (y axis)
plt.scatter(df['Cartman'], df['Stan'])
plt.title("Scatterplot showing words/episdoe for Cartman and Stan")

#@ 5
# Guess how Cartman and Stan's words/episode are correlated.
# Then compute the correlation
df[['Cartman', 'Stan']].corr()

#@ 6
# compute the covariance matrix for top 4 characters
df[top_characters[:4]].corr()

#@ 7
# compute the correlation between the 10 characters who speak the most
corr = df[top_characters[:10]].corr()


#@ 8
# create a bar plot of correlation relative to Cartman
# for the top 10 characters
# don't plot Cartman
corr['Carmen'][:1].plot

#@ 9
# if you still have time, produce a heatmap of the correlation








