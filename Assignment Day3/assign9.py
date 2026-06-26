'''

Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''
print("Accepts distance (km), mileage (km/litre), and petrol price.")
print("Calculates total fuel cost.")
dis = int(input("Enter Distance: "))
mil = int(input("Enter Mileage: "))
petrol_price = int(input("Enter petrol price: "))
total_cost = (dis/mil)*petrol_price
print(f"Cost = {total_cost}")
