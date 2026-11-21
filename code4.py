import json

# Read existing JSON file
with open("cities.json", "r") as file:
    cities = json.load(file)

# Take input from user
city = input("Enter the city name: ")
population = int(input("Enter population: "))

# Add new city
cities[city] = population

# Update JSON file
with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4)

print("Updated dictionary:", cities)


