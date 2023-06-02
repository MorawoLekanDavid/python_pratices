from die import Die
import pygal
die = Die(12)
#Holds the number of rolls in a list
def D1():
    results = []
    for roll_num in range(1000):
        result = die.rolling()
        results.append(result)
    #print(results)

#Hold the frequency of each sides in a dictionary
frequency = []#{}
for side in range(1,die.num_sides + 1):
    freq = D1.results.count(side)
    frequency.append(freq)
    #frequency['Die_side '+str(side)] = freq
print(frequency)

#Making a Histogram
hist = pygal.Bar()
hist_title = "Result of rolling one D6 100 times"
hist.x_labels = list(range(1,die.num_sides + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add('D'+str(die.num_sides),frequency)
hist.render_to_file('die_visual.svg')