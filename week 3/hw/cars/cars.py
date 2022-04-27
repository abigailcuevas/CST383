# -*- coding: utf-8 -*-
"""

Using Pandas Series.

In this assignment we use Pandas to study a data set about
cars that comes from a 1974 Motor Trend magazine.  

Please see 
https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html
for details about what the columns mean.

Note that the displacement of an engine relates to the size and power
of an engine.  It represents the total amount of volume the
cylinders of the engine displace as they more.

Each problem is defined using special comment lines:
    
#@ problem     Lines that start like this give the problem ID.

##             Lines that start like this give the problem description.

#@ assume      Lines that start like this list the variables you can refer
               to in your code.
               
#@ assign      Lines like are used when your answer should be an assignment
               statement, and give the variable to assign to.

If a problem doesn't have a #@ assign line, then your answer 
should be an expression.

Provide your answer on the first blank line after the problem lines.

In this assignment, each problem requires an expression, and requires
only one line of code.
    
Note that if you select a column of a Pandas DataFrame
(for example, with df['mpg']), the type of value you get is a Pandas
Series.

"""

# note: do not import other packages; my test script uses only these
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

#
# read the data
#

df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/mtcars.csv")

#@ problem 1
## What was the average MPG of cars like back in 1974?
## Compute the average value of the mpg series.
#@ assume df
df['mpg'].mean()

#@ problem 2
## What was the best MPG among these 1974 cars?
## Compute the maximum value of the mpg column.
#@ assume df
df['mpg'].max()

#@ problem 3
## How many different numbers of forward gears did the cars in this
## dataset have?
## Compute the counts for each of the unique values in the 'gear' column.
#@ assume df
df['gear'].value_counts()

#@ problem 4
## Do many cars have MPG that is greater than 20 MPG?
## Compute a Series containing the MPG values greater than 20.
## hint: use a boolean mask
#@ assume df
df['mpg'][df.mpg > 20]

#@ problem 5
## What fraction of the cars have an MPG higher than 22 MPG?
## Compute a value between 0 and 1 giving the fraction of the
## cars with MPG greater than 22.
## hint: the answer is short and requires mentioning df only once
#@ assume df
(df.mpg > 22).mean()


#@ problem 6
## Do many cars have MPG values that are within 20% of the top MPG value?
## Compute a Series containing the MPG values that are greater than
## 0.8 times the maximum MPG value in the data set.
## Hint: again, use a boolean mask.  To create the mask you'll
## need the max value of the MPG column.
#@ assume df
df['mpg'][df.mpg > (0.8 * df['mpg'].max()) ]


#@ problem 7
## What are the 1/4 mile times for the cars with high MPG values?
## Compute a Series containing the qsec values for the cars that
## have MPG values greater than 0.8 times the maximum MPG value
## in the data set.
## Hint: you can use the same boolean mask you used in the last
## problem, but this time use it with the Series of the qsec
## column values.
#@ assume df
df['qsec'][df.mpg > (0.8 * df['mpg'].max()) ]

#@ problem 8
## Are the gas guzzlers a lot faster than the high MPG cars?
## Compute a Series containing the qsec values for the cars that
## have MPG values less than 1.2 times the minimum MPG value
## in the data set.
#@ assume df
df['qsec'][df.mpg < (1.2 * df['mpg'].min()) ]

#@ problem 9
## Do cars with a small number of forward gears have high MPG?
## Compute a Series containing values in the mpg column for which the value in the 'gear' column is 3
## hint: index into a series of the mpg values using a boolean mask based on a series of the gear values
#@ assume df
df['mpg'][df.gear == 3]


#@ problem 10
## What about cars with a large number of forward gears?
## Compute a Series containing values in the mpg column for which the value in the 'gear' column is 5
#@ assume df
df['mpg'][df.gear == 5]

#@ problem 11
## On average, what's the MPG for cars with 3 forward gears?
## Compute the average value of the mpg values for which the corresponding 'gear' value is 3
#@ assume df
(df['mpg'][df.gear == 3]).mean()


#@ problem 12
## On average, what's the MPG for cars with 5 forward gears?
## Compute the average value of the mpg values for which the corresponding 'gear' value is 5
#@ assume df
(df['mpg'][df.gear == 5]).mean() 


#@ problem 13
## Are lighter cars faster?
## Compute the average 1/4 mile time for cars with greater than average weight.
#@ assume df
(df['qsec'][df.wt > df.wt.mean()]).mean()

#@ problem 14
## Now compare with the speed of lighter cars.
## Compute the average 1/4 mile time for cars with less than average weight.
#@ assume df
(df['qsec'][df.wt < df.wt.mean()]).mean() 

#@ problem 15
## Is there a big difference in power between cars with V6 and V8 engines?
## Calculate the average hp value for cars where vs is 0 and cyl is 8.
#@ assume df
(df['hp'][(df.vs == 0) & (df.cyl == 8)]).mean() 

#@ problem 16
## For comparison, what's the power for cars with V6 engines?
## Calculate the average hp value for cars where vs is 0 and cyl is 6.
#@ assume df
(df['hp'][(df.vs == 0) & (df.cyl == 6)]).mean() 


