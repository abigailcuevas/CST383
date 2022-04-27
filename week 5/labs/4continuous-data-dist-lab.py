# -*- coding: utf-8 -*-
"""
Probability: Continuous data distributions

@author: Glenn
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import rcParams
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

# =============================================================================
# Start of lab
# =============================================================================

# Here is a "lognormal distribution".
# rv stands for "random variable"
rv = stats.lognorm(0.5)

# plot the pdf of the random variable
# you will need function pdf()
# first use linspace to get some values from 0 to 5 
x = np.linspace(0, 5, 100)
y = rv.pdf(x)
plt.plot(x, y)

# Using your eyes, where do you think the mean is?


# find the mean by using variable rv
print(rv.mean())

# Using your eyes, where do you think the median is?


# find the median by using variable rv
print(rv.median())

# get 1000 samples from the random variable
sample = rv.rvs(size = 1000);
np.round(sample, 2)
print(np.round(sample, 2))
# plot the samples as a histogram
plt.hist(np.round(sample, 2))

# plot the samples using a density plot


# get 100 values of the pdf between 0 and 5
# Using these values, can you estimate the area under the PDF?



