'''Assignment 8: Car Mileage Calculator

 A car owner wants to calculate the mileage and fuel cost of a journey.

Create a class Car with the following attributes:

Car brand

Car model

Distance travelled in km

Fuel consumed in litres

Petrol price per litre

Create the following methods:

calculate_mileage() – Calculate kilometres per litre.

calculate_fuel_cost() – Calculate total fuel cost.

display_trip_details() – Display car and journey details.

Formulas:

Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price

Sample data:

Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105

'''

class Car:
	def attribute(self, brand, model, distance, fuel_consumed, petrol_price):
		self.brand = brand
		self.model = model
		self.distance = distance
		self.fuel_consumed = fuel_consumed
		self.petrol_price = petrol_price

	def calculate_mileage(self):
		self.mileage = self.distance / self.fuel_consumed

	def calculate_fuel_cost(self):
		self.fuel_cost = self.fuel_consumed * self.petrol_price

	def display_trip_details(self):
		print("Car Brand:", self.brand)
		print("Car Model:", self.model)
		print("Distance:", self.distance, "km")
		print("Mileage:", self.mileage, "km/l")
		print("Fuel Cost:", self.fuel_cost)


brand = input("Enter car brand: ")
model = input("Enter car model: ")
distance = float(input("Enter distance travelled in km: "))
fuel_consumed = float(input("Enter fuel consumed in litres: "))
petrol_price = float(input("Enter petrol price per litre: "))

car = Car()
car.attribute(brand, model, distance, fuel_consumed, petrol_price)
car.calculate_mileage()
car.calculate_fuel_cost()
car.display_trip_details()