import numpy as np
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2],[-12, -4], [3, 4]])
#names == "Bob
#print(~(names == "Bob"))
#print(data[~(names == "Bob") | ~(names == "Joe")])

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[0,2,3],[10,11,12]])
#concatenate arrays together. if the axis arg is set to zero which is the default val for the axis,
#  it concat it vertically
d = np.concatenate((a,b))
#vertical conc
c = np.vstack((a,b))
e = np.hstack((a,b))
print(c)
print(c.ndim)
print(c.shape)