import pandas as pd
import numpy as np

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")

dfs = df.sample(20)

new_one = (dfs - dfs.mean())/dfs.std()


print(new_one.mean())

print(new_one.max())



