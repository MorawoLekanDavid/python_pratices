from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name.lower() == country_name.lower():
            return code
    return None
#print(get_country_code("mali"))