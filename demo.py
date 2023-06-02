import matplotlib.pyplot as plt
x = list(range(1,5001))
y= [num**3 for num in x]
# Using colormap to describe the values of y
plt.scatter(x,y,c=y, cmap=plt.cm.Reds,s=10)
plt.title("A linear graph", fontsize=12)
plt.xlabel('X-axis',fontsize=12)
plt.ylabel('Y-axis',fontsize=12)
plt.tick_params(axis='x',which='major',labelsize=14) #Thickness of the interval
plt.savefig('cube_of_num.png',bbox_inches='tight') # save the original figure


