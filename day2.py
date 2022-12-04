import pandas as pd
import numpy as np
import time

# get the start time
st = time.time()

#   A = Rock        X = Rock     1   X = LOSE
#   B = Paper       Y = Paper    2   Y = DRAW
#   C = Scissors    Z = Scissors 3   Z = WIN


filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)

df.set_axis(['Opponent', 'Response'], axis=1 inplace=True)

df.loc[(df['Opponent'] == 'A') & (df['Response'] == 'X'), 'Result'] = 3
df.loc[(df['Opponent'] == 'A') & (df['Response'] == 'Y'), 'Result'] = 1
df.loc[(df['Opponent'] == 'A') & (df['Response'] == 'Z'), 'Result'] = 2
df.loc[(df['Opponent'] == 'B') & (df['Response'] == 'X'), 'Result'] = 1
df.loc[(df['Opponent'] == 'B') & (df['Response'] == 'Y'), 'Result'] = 2
df.loc[(df['Opponent'] == 'B') & (df['Response'] == 'Z'), 'Result'] = 3
df.loc[(df['Opponent'] == 'C') & (df['Response'] == 'X'), 'Result'] = 2
df.loc[(df['Opponent'] == 'C') & (df['Response'] == 'Y'), 'Result'] = 3
df.loc[(df['Opponent'] == 'C') & (df['Response'] == 'Z'), 'Result'] = 1


df.loc[(df['Response'] == 'X'), 'ThrowPoints'] = 0
df.loc[(df['Response'] == 'Y'), 'ThrowPoints'] = 3
df.loc[(df['Response'] == 'Z'), 'ThrowPoints'] = 6

df.loc[df['Result'].isnull(), 'Result'] = 0

df.loc[:,'Total'] = df.sum(axis=1)

print(df['Total'].sum())

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
