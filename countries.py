# Summary: 

# import modules
from io import TextIOBase
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

for country_code in sorted(COUNTRIES.keys()): 
    print(country_code, COUNTRIES[country_code])

# extract the country code
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #If the country was not found found, return None
    return None

print(get_country_code('Andorra'))
print(get_country_code("Nigeria"))
print(get_country_code('Texas'))
