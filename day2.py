import pandas as pd

filename = 'AOC22-D2-input.txt'

    dataframe = pd.read_csv(filename, sep=' ')
    
print(dataframe)

## dataframe.loc[:,'Total'] = dataframe.sum(axis=1)

## max_element = dataframe['Total'].max()
## print(max_element)
## print(dataframe['Total'].nlargest(n=3).sum())
