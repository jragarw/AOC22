import pandas as pd
import numpy as np

#   A = Rock        X = Rock
#   B = Paper       Y = Paper
#   C = Scissors    Z = Scissors


filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)

df.set_axis(['Opponent', 'Response'], axis=1)

df.loc[(df['Opponent'] == 'A') & (df['Response'] == 'Y'), 'Result'] = '6'
df.loc[(df['Opponent'] == 'B') & (df['Response'] == 'Z'), 'Result'] = '6'
df.loc[(df['Opponent'] == 'C') & (df['Response'] == 'X'), 'Result'] = '6'
df.loc[(df['Opponent'] == 'A') & (df['Response'] == 'X'), 'Result'] = '3'
df.loc[(df['Opponent'] == 'B') & (df['Response'] == 'Y'), 'Result'] = '3'
df.loc[(df['Opponent'] == 'C') & (df['Response'] == 'Z'), 'Result'] = '3'

df.loc[(df['Response'] == 'X'), 'ThrowPoints'] = '1'
df.loc[(df['Response'] == 'Y'), 'ThrowPoints'] = '2'
df.loc[(df['Response'] == 'Z'), 'ThrowPoints'] = '3'

df.loc[df['Result'].isnull(), 'Result'] = 0

throwtotal = df['Result'] + df['ThrowPoints']

dataframe.loc[:,'Total'] = dataframe.sum(axis=0)

print(df)
