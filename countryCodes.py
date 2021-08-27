# Summary: Extract the country code

# import modules
from pygal.maps.world import COUNTRIES

# Methods
def getCountryCode(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #If the country was not found found, return None
    return None