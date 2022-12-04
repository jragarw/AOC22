import pandas as pd
import numpy as np

filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)

conditions = [
    df.loc[df['0'] == 'A' & df.loc[df['1'] == 'Y',
    df.loc[df['0'] == 'B' & df.loc[df['1'] == 'Z',
    df.loc[df['0'] == 'C' & df.loc[df['1'] == 'Y',
    df.loc[df['0'] == 'B' & df.loc[df['1'] == 'Y',
    df.loc[df['0'] == 'C' & df.loc[df['1'] == 'Z',
]

choices = ['6','6','6','3','3','3']

df['result'] = np.select(conditions, choices, default='0')


print(df)
