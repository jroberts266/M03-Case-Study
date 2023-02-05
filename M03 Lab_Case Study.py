# M03 Lab Case Study
# Author: Joseph Roberts
# Created: 2023-02-04
# Demonstrating utilizing python classes

# Creates Vehicle class as parent class
class Vehicle():
    def __init__(self, type):
        self.type = type       

# Creates child class that inherits attribute from parent class
class Automobile(Vehicle):
    def __init__(self,type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Function that will print vehicle info when called
    def vehicle_report(self):
        print("Vehicle Type: ", self.type, " \nVehicle Year: ", self.year ,"\nVehicle Make: ", self.make, 
        "\nVehicle Model: ", self.model, "\nVehicle Doors: ", self.doors, "\nVehicle Roof: ", self.roof)

# Creates instance of automobile class    
car = Automobile('Van','2011','Chrysler','Town and Country','5','No Sunroof')

# The following variables take user inputs and assigns them to Parent and Child classes
car.type = input("enter vehicle type: ")
car.year = input("enter vehicle year: ")
car.make = input("enter vehicle manufacturer: ")
car.model = input("enter model of vehicle: ")
car.doors = input("enter number of doors on vehicle: ")
car.roof = input("enter type of roof on vehicle: ")

# Calls vehicle report function from vehicle class through inheritance
car.vehicle_report()