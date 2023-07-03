import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = np.random.standard_normal(100)
fig = plt.figure()
axes = fig.subplots(2,2)
sub1 = axes[0,0].scatter(np.arange(100),data,color='black',alpha=0.3,marker='o')
sub2 = axes[0,1].hist(np.random.standard_normal(500),color='red', bins=100)
sub3 = axes[1,0].plot(np.arange(100),data,color='blue', linestyle='dashed',alpha=0.3, marker='x')
plt.show()