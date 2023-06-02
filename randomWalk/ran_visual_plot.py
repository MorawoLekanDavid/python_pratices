import matplotlib.pyplot as plt
from random_walk import Randomwalk
while True:
# Instantiating the class Randomwalk
#For molecular motion
        rw = Randomwalk(5000)
        rw.fill_walk()
        #plt.figure(dpi=128,figsize=(10,16))
        point_num = list(range(rw.num_points))
        plt.plot(rw.x_value,rw.y_value,linewidth=2)
        #plt.axes().get_xaxis().set_visible(False)
        #plt.axes().get_yaxis().set_visible(False)
        plt.savefig('molecular_motion1_visual.png',bbox_inches='tight')
        plt.show()
        keep_running = input("Make another random walk? (y/n):")
        if keep_running =='n':
            break
