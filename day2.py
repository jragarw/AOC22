import pandas as pd
import numpy as np

filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)


conditions = [
    (df['1'].eq('Z')),
    (df['1'].eq('Y')),
    (df['1'].eq('X'))
]

values = ['3', '2', '1']

df['ThrowPoints'] = np.select(conditions, values)

print(df)
