'''
========================================
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1
'''
total_amount = int(input("Enter the total amount "))
total_10_coins = int(total_amount/10)
total_5_coins = (total_amount%10)/5
total_5_coins =int(total_5_coins)

print(f"Amount = ₹10 x {total_10_coins} , ₹5 x {total_5_coins}")