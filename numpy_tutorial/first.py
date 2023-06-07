import numpy as np
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2],[-12, -4], [3, 4]])
#names == "Bob"
print(~(names == "Bob"))
print(data[~(names == "Bob") | ~(names == "Joe")])