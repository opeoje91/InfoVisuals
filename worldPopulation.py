# Summary: Explore country data and convert population value into numerical values

# import modules
import csv

# Load the data into a list.
filename = 'population.csv'
with open(filename, newline='') as csvfile:
    pop_data = csv.reader(csvfile)

    # Print the 2010 population for each country
    for row in pop_data:
        if row[2] == '2010':
            country_name = row[0]
            population = row[3]
            print(country_name + ": " + population)

#TASK
# Convert population value into Numerical Values