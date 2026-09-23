'''Assignment 9: Product Inventory Management'''

class Product:
    def attribute(self, product_id, product_name, price, available_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.available_quantity = available_quantity

    def add_stock(self, quantity):
        self.available_quantity += quantity

    def sell_product(self, quantity):
        if quantity > self.available_quantity:
            raise ValueError("Insufficient stock")
        self.available_quantity -= quantity

    def calculate_stock_value(self):
        self.stock_value = self.price * self.available_quantity

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Available Quantity:", self.available_quantity)
        print("Total Stock Value:", self.stock_value)


product = Product()
product.attribute(int(input("Enter product ID: ")), input("Enter product name: "),
                  float(input("Enter price: ")), int(input("Enter initial quantity: ")))
product.add_stock(int(input("Enter stock to add: ")))
product.sell_product(int(input("Enter quantity to sell: ")))
product.calculate_stock_value()
product.display_product()
