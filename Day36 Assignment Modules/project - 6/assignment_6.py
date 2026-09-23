from models.customer import Customer

customers = []
for _ in range(5):
    customer_id = int(input("Enter Customer ID: "))
    customer_name = input("Enter Customer Name: ")
    city = input("Enter City: ")
    purchase_amount = int(input("Enter Purchase Amount: "))
    customers.append(Customer(customer_id, customer_name, city, purchase_amount))

print("\nAll Customers:")
for customer in customers:
    customer.display()

city_name = input("\nEnter city name to filter customers: ")
print(f"Customers from {city_name}:")
for customer in customers:
    if customer.city == city_name:
        customer.display()

print("\nCustomers with purchase amount greater than 10000:")
for customer in customers:
    if customer.purchase_amount > 10000:
        customer.display()

highest_customer = max(customers, key=lambda c: c.purchase_amount)
print(f"\nHighest Purchase Customer: {highest_customer.customer_name} {highest_customer.purchase_amount}")

total_sales = sum(customer.purchase_amount for customer in customers)
print(f"\nTotal Sales: {total_sales}")

average_purchase = total_sales / len(customers)
print(f"Average Purchase Amount: {average_purchase}")

search_id = int(input("\nSearch Customer ID: "))
found = None
for customer in customers:
    if customer.customer_id == search_id:
        found = customer
        break
if found:
    print("Customer Found:")
    found.display()
else:
    print("Customer not found")
