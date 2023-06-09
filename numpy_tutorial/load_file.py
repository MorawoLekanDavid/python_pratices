import numpy as np
from datetime import datetime

#handling a csv file and the like with numpy
filename = 'numpy_tutorial/death_valley_2014.csv'
data = np.genfromtxt(filename, delimiter=",", dtype=str)
header = [(column,col_row) for column,col_row in enumerate(data[0])]
dates = np.array([np.datetime64(datetime.strptime(date,'%Y-%m-%d')) for date in data[1:, 0]])
print(data[1:,1])
