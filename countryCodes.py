# Summary: Extract the country code

# import modules
from pygal.maps.world import COUNTRIES
import csv

# Methods
def getCountryCode(countryName):
    for code, name in COUNTRIES.items():
        if name == countryName:
            return code
    #If the country was not found found, return None
    return None

# Convert population value in form of string into Numerical Values
def convertPopValToNumericalValue(populationValue):
    return int(float(populationValue))


# get population data
def loadPopData(filename):
    popData = []
    with open(filename, newline='') as csvfile:
        csvReaderData = csv.reader(csvfile)
        # skip the headers
        next(csvReaderData, None)  
        for row in csvReaderData:
            popData.append(row)
    return popData


