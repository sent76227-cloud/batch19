'''
12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza

---'''
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]
d = {}
for i in orders:
    d[i] = d.get(i,0)+1
print(d)
max = -1
for k ,v in d.items():
    if max< v:
        max = v
for k,v in d.items():
    if max == v:
        print("Most oders food is ",k)    