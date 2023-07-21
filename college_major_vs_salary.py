# -*- coding: utf-8 -*-
"""College-Major_vs_Salary.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15-NubAcRro1zbzqatZ0hLA4uCmPuERpV
"""

import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')

df.head()

df.shape

df.columns

df.isna()

df.tail()

clean_df = df.dropna()
clean_df.tail()

clean_df['Starting Median Salary'].max()
clean_df['Starting Median Salary'].idxmax()
clean_df['Undergraduate Major'].loc[43]

# What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
clean_df['Undergraduate Major'].loc[clean_df['Mid-Career Median Salary'].idxmax()]

# Which college major has the lowest starting salary and how much do graduates earn after university?
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
clean_df['Undergraduate Major'].loc[clean_df['Mid-Career Median Salary'].idxmin()]

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

clean_df.groupby('Group').count()

pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()
