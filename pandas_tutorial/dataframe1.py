import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = pd.DataFrame(np.arange(16).reshape(4,4),index = ['ohio', 'colorado','utah','Nyc'],
                     columns = ['one','two','three','four'])
print(data)
a = data.loc[data['three'] >= 2]
b = data.iloc[:,:3][data['three'] > 5]
c = data.iloc[[1,2],[2,3,1]]
print(c)
#print(data['two'])
#print(data.loc['colorado'])
#print(data.iloc[2])hjhjh