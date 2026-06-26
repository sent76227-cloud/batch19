'''
Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
'''
print("Calculates compound interest.")
principal = int(input("Enter the principal: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time: "))
amount = principal*(1+rate/100) ** time
amount = round(amount,2)
ci = amount - principal
ci = round(ci,2)
print(f"Amount = {amount}\nCompund Interest = {ci}")
