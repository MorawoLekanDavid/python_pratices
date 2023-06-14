import numpy as np
from datetime import datetime
import pandas as pd
from pandas import Series, DataFrame
#handling a csv file and the like with numpy
filename = 'numpy_tutorial/death_valley_2014.csv'
datas = np.genfromtxt(filename, delimiter=",", dtype=str,missing_values='',filling_values=0)
data = {}
for j in range(len(datas[0])):
    data[datas[0,j]] = datas[1:,j]
    frame = pd.DataFrame(data)
print(frame.index)
