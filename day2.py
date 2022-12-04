import pandas as pd
import numpy as np

filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)

conditions = [
    (df['0'] == 'A') & (df['Type'] == 'Y'),
    (df['0'] == 'B') & (df['Type'] == 'Z'),
    (df['0'] == 'C') & (df['Type'] == 'Y'),
    (df['0'] == 'A') & (df['Type'] == 'X'),
    (df['0'] == 'B') & (df['Type'] == 'Y'),
    (df['0'] == 'C') & (df['Type'] == 'Z'),
]

choices = ['6', '6', '6','3','3','3','0']

df['color'] = np.select(conditions, choices, default='black')


print(df)
