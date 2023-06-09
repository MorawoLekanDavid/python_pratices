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

# Numpy method for a random walk
rng = np.random.default_rng(seed=12345)
draws = rng.integers(0,2,size=nsteps)
steps = np.where(draws==0,1,-1)
walks = steps.cumsum()
#print(walks)
#print(walks.min(),walks.max())
#plt.plot(walks[:nsteps])
#plt.savefig('numpy_tutorial/numpy_randomWalk.png',bbox_inches='tight')
#plt.show()

#Numpy method for many random walk
nstep = 10
nwalk = 50
rng = np.random.default_rng(seed=12345)
draws = rng.integers(0,2,size=(nwalk,nstep))
steps = np.where(draws > 0,1,-1)
walks = steps.cumsum(axis=1)
hit30 = (np.abs(walks) >= 3).any(axis=1)
#print(walks)
#print(hit30)
print(walks[hit30])
#print(walks[hit30].sum(axis=1))
print(walks[hit30].argmax(axis=1))
print(walks[hit30].mean())