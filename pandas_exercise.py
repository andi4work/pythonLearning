# pandas


import numpy as np
import pandas as pd


#SERIES details with KEY - Value pairs

names = ['Arjun', 'Avinash', 'Balaji', 'Bala']
student_id = [401, 402, 403, 404]
arr = np.array(student_id)
match = {'Arjun': 401, 'Avinash': 402, 'Balaji': 403, 'Bala': 404}

print(match)
print(pd.Series(data=names, index=student_id))

print(pd.Series(names, student_id))

print(pd.Series(arr))

print(pd.Series(match))
