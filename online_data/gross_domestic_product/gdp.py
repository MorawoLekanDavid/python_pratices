import pygal
import csv
from matplotlib import pyplot as plt
from country_code import get_country_code
#from datetime import datetime
import pygal
from pygal.style import RotateStyle as rs,LightColorizedStyle as lcs
filename = 'online_data/gross_domestic_product/gdp_1960_2020.csv'
gdp = {}
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    for row in reader:
        date = int(row[0])
        code = get_country_code(row[2])
        if date == 2020 and code:
            gdp[code] = int(row[4])
    wm_style = rs('#336699',base_color = lcs)
    wm = pygal.maps.world.World(style = wm_style)
    wm.title = "World Gross Domestic Product"
    wm.add("2020",gdp)
    wm.render_to_file("online_data/gross_domestic_product/Gdp_2020.svg")