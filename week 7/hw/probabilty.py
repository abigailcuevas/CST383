
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import patches, rcParams
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/iris.csv')
df.info()

df.head()

new_df = df.loc[:, df.columns!='species']

new_df.corr(method = 'pearson')


#2
(df['species'] == 'setosa').sum() / df.shape[0]


#3 p(species = 'setosa, sepal_length < 5)
num4 = df[df['sepal_length'] < 5]
print( (num4['species'] == 'setosa').mean())


#4 p(sepal_length < 5, species == 'setosa)
num3 = df[df['species'] == 'setosa']
print( (num3['sepal_length'] < 5).mean())


#5 P(species = Versicolor | (sepal_length > 6) & (sepal_width < 2.6))
# P( (sepal_length > 6) & (sepal_width < 2.6) | species = vericolor)


newDfff2 = df[(df['sepal_length'] > 6) & (df['sepal_width'] < 2.6)]
#print( (newDfff2['species'] == 'versicolor').mean())

#or
num5 = df[df['species'] == 'versicolor']
print( ((num5['sepal_length'] > 6) & (num5['sepal_width'] < 2.6)).mean())
