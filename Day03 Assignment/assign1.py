'''
Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
'''
print("Accepts distance (in km) and time (in hours): ")
Distance = int(input("Enter Distance: "))
Time = int(input("Enter Time: "))
Speed = int(Distance/Time)
print(f"Speed = {Speed} km/h")