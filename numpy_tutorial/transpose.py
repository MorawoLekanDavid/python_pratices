import numpy as np
# Generate a list of range 0-14 and group it into list of 3 lists with 5 elements
arr = np.arange(15).reshape(3,5)
#Tansposes arr i.e it becomes a (5,3) array
arr = arr.T
print(arr)