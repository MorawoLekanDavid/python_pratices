import requests
import pygal
from pygal.style import LightenStyle as ls, LightColorizedStyle as lcs
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: "+ f"{r.status_code}")
res_dicts = r.json()
names, stars,plot_dicts =[],[],[]
for res_dict in res_dicts['items']:
    stars.append(res_dict['stargazers_count'])
    names.append(res_dict['name'])
    plot_dict = {
        'value': res_dict['stargazers_count'],
        'Label': res_dict['description'],
        'xlink': res_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
print(names)
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
hist.title = "Most-Starred Python Projects on GitHub"
hist.x_labels = names
hist.add("",plot_dicts)