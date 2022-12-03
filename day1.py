import pandas as pd

filename = 'AOC22-D1-input.txt'


with open(filename) as f:
    data = [list(map(int, row.split())) for row in f.read().split('\n\n')]

dataframe = pd.DataFrame(data)

print(dataframe)


