from die import Die
#import pygal
import matplotlib.pyplot as plt
die_1 = Die(12)
die_2 = Die(8)
#Holds the number of rolls in a list

results = []
for roll_num in range(1000):
    result = die_1.rolling() * die_2.rolling()
    results.append(result)
#print(results)

#Hold the frequency of each sides in a dictionary
frequency = []#{}
max_result = die_1.num_sides * die_2.num_sides
for side in range(1,max_result + 1):
    freq = results.count(side)
    frequency.append(freq)
    #frequency['Die_side '+str(side)] = freq
print(frequency)

#Making a Histogram
point_num = list(range(1,max_result+1))
plt.scatter(point_num,frequency,c=frequency,cmap=plt.cm.Blues, edgecolors='none',s=10)
plt.savefig('RollingDice/dice_rolling_scatter.png',bbox_inches='tight')
plt.show()