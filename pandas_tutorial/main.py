import numpy as np 
import pandas as pd
from pandas import Series,DataFrame

country_code = {'Nigeria':"NG",
                'United state Of America':"USA",
                'Rwanda':'RW',
                'Ghana':'GH'
                }
obj = pd.Series(country_code)
obj.name = 'Population'
#Overrodes the intial indexing
obj.index = [0,1,2,3]
obj.index.name = 'Country'
print(obj)

