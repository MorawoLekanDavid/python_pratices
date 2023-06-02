import json
import pygal
from pygal.style import RotateStyle as rs,LightColorizedStyle as lcs
from country_codes import get_country_code
filename = 'online_data/population/population_data.json'
population = {}
cc_popn1,cc_popn2,cc_popn3 = {},{},{}
with open(filename) as f:
    pop_data = json.load(f)
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            popn = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                population[code] = popn
                for cc,pop in population.items():
                    if pop < 10000000:
                        cc_popn1[cc] = pop
                    elif pop < 1000000000:
                        cc_popn2[cc] = pop
                    else:
                        cc_popn3[cc] = pop
            else:
                print(f"Error:{country_name}")
    print(len(cc_popn1),len(cc_popn2),len(cc_popn3))
    
    wm_style = rs('#336699',base_style=lcs)
    wm = pygal.maps.world.World(style = wm_style)
    wm.title = "World Population in 2010 by country"
    wm.add("< 10000000",cc_popn1)
    wm.add("< 1000000000 ",cc_popn2)
    wm.add("> 1000000000",cc_popn3)
    wm.render_to_file('online_data/population/worldPop_grouping.svg')