import pandas as pd

filename = 'AOC22-D1-input.txt'

with open(filename) as f:
    data = [list(map(int, row.split())) for row in f.read().split('\n\n')]

dataframe = pd.DataFrame(data)

dataframe.loc[:,'Total'] = dataframe.sum(axis=1)

max_element = dataframe['Total'].max()
print(max_element)
print(dataframe['Total'].nlargest(n=3).sum())
