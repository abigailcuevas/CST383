    # -*- coding: utf-8 -*-
"""
Aggregation in Lyft San Francisco bike ride-sharing data, April, 2019.

Data source:
    https://www.kaggle.com/jolasa/bay-area-bike-sharing-trips

Some of the questions we'll look into:
    - what are the ages of the riders?
    - how long are typical rides (in terms of time)
    - does riding behavior depend on age?
    - does riding behavior depend on gender?
    - does riding behavior depend on whether rider is a subscriber or a casual
      rider?
    - which start/stop locations are most common?

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

Use no loops.  Almost every problem can easily be done in one line of code.
    
@author: Glenn Bruns

"""

import numpy as np
import pandas as pd

# =============================================================================
# Read the data
# =============================================================================

df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/lyft-2019-04.csv")

# =============================================================================
# Data preprocessing
# =============================================================================

df.info()

# drop NAs
df.isna().mean().sort_values()
df.dropna(inplace=True)

# create new variable showing member age
df['member_age'] = (2019 - df['member_birth_year']).astype(int)
df = df[df['member_age'] < 100]

# great new variable showing member age group
age_groups = [18, 25, 35, 50, 100]
group_names = ['18-25', '25-35', '35-50', '>50']
df['age_group'] = pd.cut(df['member_age'], age_groups, labels=group_names).astype(object)

# drop the month column
df.drop('month', axis=1, inplace=True)


#@ problem 1
## Add new integer variable 'trip_min' to df.
## Compute this using existing variable 'trip_duration_sec'.
## Hint: use astype() to convert from float to int.
## The "assign df" below means the df dataframe, or part of it,
## will be assigned to.  Your answer will be a statement.
#@ assume df
#@ assign df
df['trip_min'] = (df['trip_duration_sec']).astype(int)


#@ problem 2
## Make start_station_id variable into int type.
#@ assume df
#@ assign df
df['start_station_id'] = (df['start_station_id']).astype(int)


#@ problem 3
## Make end_station_id variable into int type.
#@ assume df
#@ assign df
df['end_station_id'] = (df['end_station_id']).astype(int)


#@ problem 4
## Create a new column of df called 'route' that contains the
## start_station_id and the end_station_id, with '->' between
## them.  For example, if the value of start_station_id on a
## row is 1, and the end_station_id is 2, then the value of
## route for that row should be the string '1->2'.
#@ assume df
#@ assign df
df['route'] = (df['start_station_id']).astype(str) + '->' + (df['start_station_id']).astype(str)


#@ problem 5
## create a new column of df called 'BART' that is True if either the start
## or end station name contains 'BART'
#@ assume df
#@ assign df
df['BART'] = (df['start_station_name'] == 'BART' ) | (df['end_station_name'] == 'BART' )

# =============================================================================
# Data exploration
# =============================================================================

#@ problem 6
## how many rows in dataframe df?
#@ assume df
df.shape[0]


#@ problem 7
## what are the column names of df?
#@ assume df
df.columns


#@ problem 8
## what is the length of the longest trip, in hours
#@ assume df
(df['trip_duration_sec']).max() / 3600.00


#@ problem 9
## what is the median trip length, in minutes?
#@ assume df
((df['trip_min']).median())

#@ problem 10
## What is the age of the oldest rider?
#@ assume df
df['member_age'].max()


#@ problem 11
## What is the age of the youngest rider?
#@ assume df
df['member_age'].min()


#@ problem 12
## Compute the first 10 rows of df, using only columns trip_min, member_age, 
## member_gender, and user_type (in that order).
#@ assume df
df[:10][['trip_min', 'member_age', 'member_gender', 'user_type']]


#@ problem 13
## What are the unique values in column user_type?
#@ assume df
(df['user_type']).unique()


#@ problem 14
## What fraction of the user_type values are 'Subscriber'?
## Remember, a fractional value is between 0 and 1.
#@ assume df
(df['user_type'] == 'Subscriber').mean()


#@ problem 15
## Are the bikes mostly used for commuting or for pleasure?
## Compute the fraction of rides that last more than 1 hour.
#@ assume df
(df['trip_duration_sec'] > 3600).mean()


#@ problem 16
## What are the station names?
## Compute the unique station names from column 'start_station_name',
## and assign the value to variable 'station_names'.  The value of
## station_names must be a Pandas Series!
#@ assume df
#@ assign station_names
station_names = pd.Series((df['start_station_name']).unique())


#@ problem 17
## What fraction of the station names contain the word 'Station'?
## Use variable station_names to compute this.
#@ assume station_names
(station_names.str.contains('Station')).mean()


#@ problem 18
## What fraction of the rides end at a station contining the word 'Station'?
## Use df to compute this.
#@ assume df
(df['end_station_name'].str.contains('Station')).mean()


#@ problem 19
## What fraction of rides either start or stop (or both) at a station with
## BART in the name?
## Use the BART variable of df to compute this.
#@ assume df
((df['end_station_name'].str.contains('BART')) | (df['start_station_name'].str.contains('BART'))).mean()

# =============================================================================
# Aggregation with value_counts()
# =============================================================================

#@ problem 20
## How many rides are associated with each user type?
#@ assume df
df['user_type'].value_counts()


#@ problem 21
## What fraction of the rides are associated with each gender? 
## Hint: Read the pandas documentation for value_counts(), especially
## the documenation on option 'normalize'.
#@ assume df
(df['member_gender'].value_counts())/ df.shape[0]


#@ problem 22
## What fraction of the rides are associated with each age group?
## (list largest fraction first)
#@ assume df
(df['age_group'].value_counts())/ df.shape[0]


#@ problem 23
## What fraction of the rides are associated with each age group?
## (list in order of age ranges, youngest first)
## (Hint: use fancy indexing, .loc, and the group_names variable)
#@ assume df,group_names
((df['age_group'].value_counts())/ df.shape[0]).sort_index()


#@ problem 24 
## How many rides are associated with each end station name?
## (list station that occurs that most first, and show only
## the top 20 stations)
#@ assume df
df['end_station_name'].value_counts()[:20]

#@ problem 25
## How many rides are associated with each start station name?
## (list station that occurs that most first, and show only
## the top 20 stations)
#@ assume df
df['start_station_name'].value_counts()[:20]


#@ problem 26
## How many rides are associated with each combination of
## start and end stations?
## Compute the number of rides associated with the 20 most
## common combinations of start and end stations.
## Use value_counts(), and use the 'start_station_name' and
## 'end_station_name' columns of df.  Do not use the 'route' column.
## (Hint: .value_counts() can be applied to Pandas data frames,
## not just Pandas series.)
#@ assume df
df[['start_station_name','end_station_name']].value_counts()[:20]


#@ problem 27
## Which are the most-used routes?
## Compute the number of rides associated with the 20 most-used routes,
## then assign the route values to new Series variable top_routes.
#@ assume df
#@ assign top_routes
top_routes = pd.Series(df['route'].value_counts()[:20])


# =============================================================================
# Aggregation with groupby()
# =============================================================================


#@ problem 28
## Do different age groups ride for different amounts of time?
## What is the average trip time (in minutes) for each age group?
## Hint: use groupby().
#@ assume df
(df.groupby('age_group')['trip_min'].mean()) 


#@ problem 29
## The median trip length may be better then the average trip length.
## (Average trip length is heavily influenced by long rides.)
## What is the median trip time (in minutes) for each age group?
#@ assume df
(df.groupby('age_group')['trip_min'].median()) 


#@ problem 30
## Do subscribers tend to be older or younger than casual riders?
## Compute the median member age for each user type.
#@ assume df
(df.groupby('age_group')['trip_min'].median())   


#@ problem 31
## Do men tend to ride for a longer period of time then women, or
## vice versa?
## Compute the median trip length (in minutes) for each value of
## member_gender.
#@ assume df
(df.groupby('member_gender')['trip_min'].median())

#@ problem 32
## Looking at riders in terms of gender and age group, are there
## differences in trip length?
## Compute the median trip length for each combination of member_gender
## and age_group.
#@ assume df
(df.groupby(['member_gender', 'age_group'])['trip_min'].median())



#@ problem 33
## Compute the mean and median trip length (in minutes) for each age group.
#@ assume df
(df.groupby('age_group')['trip_min'].aggregate([np.mean , np.median ]) )  


#@ problem 34
## Maybe commuters tend to be subscribers, rather than casual users.
## Compute, for the case where the end station name contains "BART",
## and for the case where the end station name does not contain "BART",
## the fraction of trips in which user_type is Subscriber.
## Your answer should be a Pandas Series.
## Use group_by().
#@ assume df
df.user_type.str.contains('Subscriber').groupby(df.end_station_name.str.contains("BART")).mean()

#@ problem 35
## Do commuters tend to be younger or older often than casual riders?
## To try to answer this question, compute the median age of riders for
## 1) rides that that end at a station with 'Station' in its name, and
## 2) rides that don't end at a station with 'Station' in its name. 
## Use groupby().
#@ assume df
df.member_age.groupby(df.end_station_name.str.contains("Station")).median()


#@ problem 36
## Do trips on common routes tend to have about the same trip time?
## Answer this question with two lines of code.  First create a
## data frame (you could call it df_top_routes) that contains all the
## rows of df in which the value of 'route' in in 'top_routes'.
## Second, compute the median trip_min for each route in the new data frame.
## The median trip values should be given in descending order.
#@ assume df,top_routes


# =============================================================================
# Aggregation with crosstab()
# =============================================================================

# Aggregation is most commonly used with one categorical variable
# and one quantitative variable.  For example, get the average
# ride distance (quantitative variable) for each age group
# (categorical variable).
# When we have two categorical variables, it is common to use
# the Pandas crosstab() function, which we'll cover in class soon.

#@ problem 37
## What fraction of the rides are in each combination of user_type
## and age_group?
## Hint: use pd.crosstab() on two columns of df.
#@ assume df
pd.crosstab(df['user_type'], df['age_group']).mean()

