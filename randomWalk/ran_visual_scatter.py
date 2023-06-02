import matplotlib.pyplot as plt
from random_walk import Randomwalk
while True:
# Instantiating the class Randomwalk
    rw = Randomwalk(50000)
    rw.fill_walk()
    #plt.figure(dpi=128,figsize=(10,16))
    point_num = list(range(rw.num_points))
    plt.scatter(rw.x_value,rw.y_value,c=point_num,cmap=plt.cm.Blues, edgecolors='none',s=10)
    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolors='none',s=100)
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    plt.savefig('random_scatter_visual2.png',bbox_inches='tight')
    plt.show()
    keep_running = input("Make another random walk? (y/n):")
    if keep_running =='n':
       break
