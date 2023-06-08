from random import randint
import matplotlib.pyplot as plt
import numpy as np
# Pure python mehod of a random walk
n_pos = 0
walk = [n_pos]
nsteps = 1000
for i in range(nsteps):
    step = 1 if randint(0,1) else -1
    n_pos += step
    walk.append(n_pos)
#print(walk)
#plt.plot(walk[:100])
#plt.show()

# Numpy method
rng = np.random.default_rng(seed=12345)
draws = rng.integers(0,2,size=nsteps)
steps = np.where(draws==0,1,-1)
walks = steps.cumsum()
print(walks)
print(walks.min(),walks.max())
plt.plot(walks[:nsteps])
plt.savefig('numpy_tutorial/numpy_randomWalk.png',bbox_inches='tight')
plt.show()