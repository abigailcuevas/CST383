import pandas as pd
import seaborn as sns
import numpy as np

infile = "https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv"
df = pd.read_csv(infile)

#3
df.info()

#4
print(df.isna().sum().sum())

#5
print((df == 0).sum())


#6
df['contbr_employer'].value_counts().head(n=20)


#8
print ( df['memo_cd'].unique() )
print( df['memo_cd'].isna().mean())