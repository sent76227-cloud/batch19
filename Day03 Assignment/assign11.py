'''
Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
'''
hours = int(input("Enter Hours: "))
min = int(input("Enter Min: "))
sec = int(input("Enter Seconds: "))
hours_to_sec = hours * 3600
min_to_sec = min*60
total_seconds = hours_to_sec + min_to_sec + sec
print(f"Total Seconds = {total_seconds}")