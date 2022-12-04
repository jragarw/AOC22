import pandas as pd
import numpy as np

filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)

conditions = [
    (df['0'] == 'A') & (df['1'] == 'Y'),
    (df['0'] == 'B') & (df['1'] == 'Z'),
    (df['0'] == 'C') & (df['1'] == 'Y'),
    (df['0'] == 'A') & (df['1'] == 'X'),
    (df['0'] == 'B') & (df['1'] == 'Y'),
    (df['0'] == 'C') & (df['1'] == 'Z'),
]

choices = ['6','6','6','3','3','3']

df['result'] = np.select(conditions, choices, default='0')


print(df)
