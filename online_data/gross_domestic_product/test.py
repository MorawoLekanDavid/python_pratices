import pygal
import csv
from matplotlib import pyplot as plt
from country_code import get_country_code
from datetime import datetime
from pygal.style import RotateStyle as rs,LightColorizedStyle as lcs
filename = 'online_data/gross_domestic_product/gdp_1960_2020.csv'
gdp = []
dates = []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    for row in reader:
        for country in row[0]:
            code = get_country_code(country)
        #if code == 'rw':
            #date = datetime.strptimes(str(row[0]), '%Y-%m-%d')
            dates.append(str(row[0]))
            gdp.append(int(row[4]))
    print(dates)
    print(gdp)
    wm_style = rs('#336699',base_color = lcs)
    wm = pygal.maps.world.World(style = wm_style)
    wm.title = "World Gross Domestic Product"
    wm.add(f"{code}",gdp)
    wm.render_to_file("online_data/gross_domestic_product/Gdp_1960_2020.svg")