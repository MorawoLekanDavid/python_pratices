import pygal
import csv
from country_code import get_country_code
from pygal.style import LightenStyle as ls,LightColorizedStyle as lcs
filename = 'online_data/gross_domestic_product/gdp_1960_2020.csv'
gdp = []
dates = []
cc = get_country_code('Nigeria')
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    for row in reader:
        code = get_country_code(row[2])
        if code == cc:
            dates.append(str(row[0]))
            gdp.append(int(row[4]))
    my_style = ls('#333366', base_style=lcs)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_size = 18
    my_config.truncate_label = 15
    my_config.show_legend = False
    my_config.show_y_guides= False
    my_config.width = 1000
    hist = pygal.Bar(my_config,style=my_style)
    hist.title = f"Gross Domestic Product of {cc} between the years {int(dates[0])} - {int(dates[-1])}"
    hist.x_labels = dates
    hist.x_title = "Date of Observation"
    hist.y_title = f"Gross Domestic Product"
    hist.add("",gdp)
    hist.render_to_file('online_data/gross_domestic_product/Gdp_1960_2020.svg')
    