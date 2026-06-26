'''
Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
'''
total = int(input("Enter Total Marks: "))
obtained = int(input("Enter Obtained: "))
per = int((obtained/total) * 100)
print(f"Percentage = {per}%")