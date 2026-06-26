
'''
========================================
Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0
'''
total_bill = int(input("Enter total bill "))
total_friends = int(input("no. of friends "))
split = float(total_bill/total_friends)
print(f"Total bill = {total_bill}\nFriends = {total_friends}\nEach should pay = {split}")