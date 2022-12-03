import pandas as pd
import numpy as np

filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)

conditions = [
    (df['1'] == 'X'),
    (df['1'] == 'Y'),
    (df['1'] == 'Z')]
choices = ['1', '2', '3']
df['ThrowCost'] = np.select(conditions, choices, default='NaN')

print(df)
