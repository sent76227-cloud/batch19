'''
Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
'''

print("Accepts total amount.")
print("Calculates 10% discount and final price.")

amount = int(input("Enter amount: "))
disc = int(amount * 0.1)
total = int(amount - disc)
print(f"Discount = {disc}\nFinal = {total}")
