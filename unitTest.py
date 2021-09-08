# Summary: Test functions 

# import modules
import countryCodes as cc

# Methods: Test valid function
print(cc.getCountryCode('Andorra'))
print(cc.getCountryCode("Nigeria"))

#test invalid function
print(cc.getCountryCode('Texas'))

#test numerical value of population
populationData = cc.loadPopData("population.csv")
print(f'{populationData[0][0]} : {cc.convertPopValToNumericalValue(populationData[0][3])}')

