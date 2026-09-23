'''Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0

'''
class Product:
    def __init__(self,product_id,product_name,quatity,price_per_item):
        self.product_id = product_id
        self.product_name =product_name
        self.quatity = quatity
        self.price_per_item = price_per_item
    def calculation(self):
        self.total = self.quatity *self.price_per_item
        if self.total > 5000:
            self.dis = (10/100)*self.total
        else:
            self.dis = (5/100)*self.total
        self.final =self.total - self.dis
    def display (self):
        print("Product Id: ",self.product_id)
        print("Product Name: ",self.product_name)
        print("Quantity: ",self.quatity)
        print("Price per item: ",self.price_per_item)
        print("Total Amount, ",self.total)
        print("Discount: ",self.dis)
        print("Final Amount: ",self.final)



product_id = input("Enter Product Id")
product_name = input("Enter Product name: ")
quatity = int(input("Enter quantity: "))
price_per_item = int(input("Enter price per item: "))


p1 = Product(product_id,product_name,quatity,price_per_item)
p1.calculation()
p1.display()
            
        