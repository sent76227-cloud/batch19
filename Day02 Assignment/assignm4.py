'''
========================================
Assignment 4: Travel Fare Calculator
========================================
A cab company charges ₹15 per kilometer.

Write a Python program that:
- Accepts the number of kilometers traveled.
- Calculates the total fare.
- Displays the result.

Example:
Distance = 20 km
Total fare = ₹300
'''
number_of_km = int(input("Enter total km "))
total_fare = number_of_km * 15
print(f"Distance = {number_of_km} km\nTotal fare = ₹{total_fare}")
