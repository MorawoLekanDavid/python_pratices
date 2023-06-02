#import matplotlib.pyplot as plt
import pygal
from random_walk import Randomwalk
while True:
# Instantiating the class Randomwalk
    rw = Randomwalk(100)
    rw.fill_walk()
    #Making a Histogram
    hist = pygal.Bar()
    hist_title = "Result of rolling one D6 100 times"
    hist.x_labels = list(range(rw.num_points))
    hist.x_title = "Result"
    hist.y_title = "Frequency of result"
    hist.add('RW',rw.y_value)
    hist.render_to_file('randomwalk/random_scatter_visual.svg')
    keep_running = input("Make another random walk? (y/n):")
    if keep_running =='n':
       break
