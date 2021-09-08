# Summary: 

# import modules
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

for countryCode in sorted(COUNTRIES.keys()): 
    print(countryCode, COUNTRIES[countryCode])



