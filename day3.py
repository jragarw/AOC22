import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import time

# get the start time
st = time.time()

filename = 'AOC22-D3-input.txt'

df = pd.read_csv(filename, sep='/n', header = None)

df.set_axis(['BackpackFull'], axis=1)

df['BackpackCompLen'] = df['BackpackFull'].apply(len).div(2)




print(df)


# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
