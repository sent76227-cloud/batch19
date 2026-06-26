'''
Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
'''
dis = int(input("Enter Distance in km : "))
mil = int(input("Enter Mileage in km/litre: "))
pet_pri = int(input("Enter Pertrol price in litre: "))

total_petrol_used =  dis/mil
total_expense = pet_pri * total_petrol_used

print(f"Petrol Used = {total_petrol_used}\nTotal Cost = {total_expense}")
