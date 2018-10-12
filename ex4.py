# This creates a variable named "cars" and gives it a value of 100
cars =  100
# This creates a variable named "space_in_a_car" and gives it a value of 4.0
space_in_a_car = 4.0
# This creates a variable named "drivers" and gives it a value of 30
drivers = 30
# This creates a variable named "passengers" and gives it a value of 90
passengers = 90
# This creates a variable named "cars_not_driven" and gives it a value of (cars - drivers)
cars_not_driven = cars - drivers
# This creates a variable called cars_driven and gives it a value equal to drivers
cars_driven = drivers
# This creates a variable called "carpool_capacity" and gives it a value equal to the number of cars driven * space in a car
carpool_capacity = cars_driven * space_in_a_car
# This creates a variable called "average_passengers_per_car" and gives it a value equal to the number of passengers divided by the number of cars driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
