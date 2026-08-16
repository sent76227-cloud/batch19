'''
Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600
'''
units = int(input("Enter units: "))
bill = 6*units
print(f"Bill = {bill}")