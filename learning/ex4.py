#Price of a car
cars = 100
#Capacity of the car
space_in_a_car = 4.0
#No. of drivers
drivers = 30
#No. of passengers
passengers = 90
#No. of available cars
cars_not_driven = cars - drivers
#Assiging value of cars driven to no. of drivers
cars_driven = drivers
#No. of people that the car can take
carpool_capacity = cars_driven * space_in_a_car
#Average of the number of passengers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("Theres are only", drivers, "drivers availabale.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
