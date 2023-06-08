import numpy as np 
sample = np.arange(100).reshape((10,10))
#compute the sum of all the array of numbers
s = sample.sum()
#sum the the row element  of the array
rs = sample.sum(axis=0)
#sum the the column element  of the array
cs = sample.sum(axis=1)
#print(s,rs,cs)
#print((sample < 0).sum())
x = np.array([1,2,3,4,5,2,5,3,7])
y = np.array([1,2,3,4,5,6,7,8,9,10,11])
res = np.intersect1d(x,y)
print(np.unique(x))