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
                                      
df.loc[df['Result'].isnull(), 'Result'] = 0
                                      
print(df)
