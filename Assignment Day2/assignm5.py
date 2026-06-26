'''
========================================
Assignment 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240
'''
cart_total = int(input("The card total amount "))
calculates_tax = int(cart_total * 0.12)
total = int(calculates_tax + cart_total)

print(f"Cart = ₹{cart_total}\nTax = ₹{calculates_tax}\nTotal = ₹{total}")