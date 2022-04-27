import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# plotting - change as desired
sns.set()
sns.set_context('talk')   
sns.set_style('whitegrid')

df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv")
# 5
df.drop(['usid', 'fnlwgt'], axis=1)
# 6
df.head()
# 7
df['education_num'].describe()
# 8
plt.hist(df['education_num']);
plt.xlabel('years of education')
#9
df['education_num'].value_counts(normalize=True).sort_index(ascending=True).cumsum()[:15].plot.bar()

#10
sns.kdeplot(df.capital_gain)