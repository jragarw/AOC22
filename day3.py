import pandas as pd

filename = 'AOC22-D3-input.txt'

df = pd.read_csv(filename, sep='/n', header = None)

df.set_axis(['BackpackFull'], axis=1)

df['BackpackLength'] = df['BackpackFull'].apply(len).div(2)




print(df)
