'''
Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
'''
amount = int(input("Enter Amount: "))
hund = int(amount/100)
fifty = amount%50
ten = fifty%10
print(f"{hund} , {fifty}, {ten}")
