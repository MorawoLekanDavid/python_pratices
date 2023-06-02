import json
import pygal
from country_codes import get_country_code
filename = 'online_data/population/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            popn = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                print(f"{code}:{popn}")
            else:
                print(f"Error:{country_name}")
    wm = pygal.maps.world.World()
    wm.title = "North, Central, and South America"
    wm.add("North America",['ca','mx','us'])
    wm.add("Central America", ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
    wm.add("South America",  ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
    #wm.add("West Africa",  ['bf', 'bj', 'tg', 'gh', 'ci', 'lr', 'sl','gn', 'gw', 'sn', 'mr', 'gm', 'ne','cv','ng','ml'])
    wm.render_to_file('online_data/population/americas.svg')