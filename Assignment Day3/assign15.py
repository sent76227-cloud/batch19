'''
Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
'''
dis1 = int(input("Enter Distance1: "))
time1 = int(input("Enter time1: "))
dis2 = int(input("Enter Distance2: "))
time2 = int(input("Enter time2: "))
speed1 = dis1/time1
speed2 = dis2/time2
avg_speed = (speed1 + speed2)/2
avg_speed = int(avg_speed)
print(f"Average Speed = {avg_speed} km/h")