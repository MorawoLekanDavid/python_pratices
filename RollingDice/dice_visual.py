from die import Die
import pygal
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
hist = pygal.Bar()
hist_title = "Result of rolling one D6 100 times"
hist.x_labels = list(range(1,max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add('D'+str(die_1.num_sides)+','+str(die_2.num_sides),frequency)
hist.render_to_file('RollingDice/dice_visual.svg')