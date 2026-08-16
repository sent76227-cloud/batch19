'''QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3'''

from collections import namedtuple

order = namedtuple("Order", ["order_id", "customer_name", "product_name", "amount"])

n = int(input("Enter number of orders: "))

orders = []

# 1. Read order records
for i in range(n):
    order_id, customer_name, product_name, amount = input().split()

    o = order(order_id, customer_name, product_name, int(amount))
    orders.append(o)


# 2. Display all order details
print("\nAll Orders:")

for o in orders:
    print(o.order_id, o.customer_name, o.product_name, o.amount)


# 3. Find order having highest amount
highest = orders[0]

for o in orders:
    if o.amount > highest.amount:
        highest = o

print("\nHighest Value Order:")
print(highest.order_id, highest.customer_name, highest.product_name, highest.amount)


# 4. Calculate total sales
total = 0

for o in orders:
    total += o.amount

print("\nTotal Sales:")
print(total)


# 5. Count orders above 10000
count = 0

for o in orders:
    if o.amount > 10000:
        count += 1

print("\nOrders Above ₹10,000:")
print(count)
