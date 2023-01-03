# pandas


import numpy as np
import pandas as pd

from numpy.random import randn

# SERIES details with KEY - Value pairs

names = ['Arjun', 'Avinash', 'Balaji', 'Bala']
student_id = [401, 402, 403, 404]
arr = np.array(student_id)
match = {'Arjun': 401, 'Avinash': 402, 'Balaji': 403, 'Bala': 404}

# print(match)
# print(pd.Series(data=names, index=student_id))
# print(pd.Series(names, student_id))
# print(pd.Series(arr))
# print(pd.Series(match))

# Dataframes

print(np.random.seed(101))

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

# print(df)
#
# print(df['W'])
#
# print(df[['X','Z']])

print(df.drop('X', axis=1,inplace=True))

print(df.drop('E',axis=0,inplace=True))
print(df)