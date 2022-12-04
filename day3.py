import pandas

filename = 'AOC22-D2-input.txt'

df = pd.read_csv(filename, sep=' ', header = None)

df.set_axis(['BackpackFull'], axis=1)


print(df)
