'''
Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
'''
cost_price =int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))
profit = selling_price - cost_price
profit_per = (profit/cost_price)*100
print(f"Profit = {profit}\nProfit % = {profit_per}")