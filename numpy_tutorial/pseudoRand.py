import numpy as np
import matplotlib.pyplot as plt
points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
z = np.sqrt(xs**2 + ys**2)
#print(z)
plt.plot(z,cmap=plt.cm.gray,extent=[-5,5,-5,5])
plt.colorbar()