import pandas as pd
import numpy as np

filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)

df.set_axis(['Opponent', 'Response'], axis=1)

conditions = [
    df.loc[df['Opponent'] == 'A' & df.loc[df['Response'] == 'Y',
    df.loc[df['Opponent'] == 'B' & df.loc[df['Response'] == 'Z',
    df.loc[df['Opponent'] == 'C' & df.loc[df['Response'] == 'Y',
    df.loc[df['Opponent'] == 'B' & df.loc[df['Response'] == 'Y',
    df.loc[df['Opponent'] == 'C' & df.loc[df['Response'] == 'Z',
]

choices = ['6','6','6','3','3','3']

df['result'] = np.select(conditions, choices, default='0')


print(df)
