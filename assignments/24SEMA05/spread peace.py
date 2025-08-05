temperatures = [23.4, 22.1, 21.8, 24.0, 23.9, 22.5, 21.7]
total = sum(temperatures)
count = len(temperatures)
average_temp = total / count
print("Average temperature over the week:", average_temp)
def growth_rate(current, previous):
    if previous == 0:
        return None
    return (current - previous) / previous * 100

print(growth_rate(120, 100))

gdp_values = [4.2,1.4,6.7,5.8,7.1,3.5,2.9]

# Basic loop to find countries with GDP greater than 3.0 
for gdp in gdp_values:
    if gdp > 3.0:
        print("Country with GDP greater than 3.0:")

# To get the list of countries with GDP greater than 3.0
high_gdp_countries = [gdp for gdp in gdp_values if gdp > 3.0]
print("Countries with GDP greater than 3.0:", high_gdp_countries)

#Avergage GDP calculation
total_gdp = sum(gdp_values)
count_countries = len(gdp_values)
average_gdp = total_gdp / count_countries
print("Average GDP of the countries:", average_gdp)

temperature_data = [2.4, 6.7, 45, 67, 23.4, 22.1, 21.8, 24.0, 23.9, 22.5, 21.7, 32.5, 30.0, 29.8]

# Categorizing temperatures
for temp in temperature_data:
    if temp < 10:
        print("Cold")
    elif 10 <= temp <= 25:
        print("Mild")
    else:
        print("High")