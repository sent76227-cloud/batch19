'''6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
'''
n = int(input("Enter number of products: "))

products = []

# Read product details
for i in range(n):
    product_id, product_name, price = input().split()

    p = (product_id, product_name, int(price))
    products.append(p)


# Display all products
print("\nAll Products:")

for p in products:
    print(p)


# Find costliest product
costliest = products[0]

for p in products:
    if p[2] > costliest[2]:
        costliest = p

print("\nCostliest Product:")
print(costliest)


# Find cheapest product
cheapest = products[0]

for p in products:
    if p[2] < cheapest[2]:
        cheapest = p

print("\nCheapest Product:")
print(cheapest)


# Calculate average price
total = 0

for p in products:
    total += p[2]

average = total / n

print("\nAverage Price:")
print(average)


# Display products above 50000
print("\nProducts Above ₹50,000:")

for p in products:
    if p[2] > 50000:
        print(p)