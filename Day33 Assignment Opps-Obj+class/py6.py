'''

class ElectricityBill:
	def attribute(self, consumer_number, consumer_name, units_consumed,
				  rate_per_unit, fixed_charge):
		self.consumer_number = consumer_number
		self.consumer_name = consumer_name
		self.units_consumed = units_consumed
		self.rate_per_unit = rate_per_unit
		self.fixed_charge = fixed_charge

	def calculate_energy_charge(self):
		self.energy_charge = self.units_consumed * self.rate_per_unit

	def calculate_total_bill(self):
		self.total_bill = self.energy_charge + self.fixed_charge

	def display_bill(self):
		print("Consumer Number:", self.consumer_number)
		print("Consumer Name:", self.consumer_name)
		print("Energy Charge:", self.energy_charge)
		print("Total Bill:", self.total_bill)


consumer_number = int(input("Enter consumer number: "))
consumer_name = input("Enter consumer name: ")
units_consumed = float(input("Enter units consumed: "))
rate_per_unit = float(input("Enter rate per unit: "))
fixed_charge = float(input("Enter fixed charge: "))

bill = ElectricityBill()
bill.attribute(consumer_number, consumer_name, units_consumed,
			   rate_per_unit, fixed_charge)
bill.calculate_energy_charge()
bill.calculate_total_bill()
bill.display_bill()
Assignment 6: Electricity Bill Calculator

An electricity board wants to calculate a customer's electricity bill based on units consumed.

Create a class ElectricityBill with the following attributes:

Consumer number

Consumer name

Units consumed

Rate per unit

Fixed charge

Create the following methods:

calculate_energy_charge() – Calculate units × rate per unit.

calculate_total_bill() – Add energy charge and fixed charge.

display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600
'''


        