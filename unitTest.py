# Summary: Test functions 

# import modules
import countryCodes as c

# Methods: Test valid function
print(c.getCountryCode('Andorra'))
print(c.getCountryCode("Nigeria"))

#test invalid function
print(c.getCountryCode('Texas'))
