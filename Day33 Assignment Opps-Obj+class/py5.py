'''Assignment 5: Shopping Bill Calculator'''

class ShoppingBill:
    def attribute(self, product_name, product_price, quantity, discount_percentage, gst_percentage):
        self.product_name = product_name
        self.product_price = product_price
        self.quantity = quantity
        self.discount_percentage = discount_percentage
        self.gst_percentage = gst_percentage

    def calculate_subtotal(self):
        self.subtotal = self.product_price * self.quantity

    def calculate_discount(self):
        self.discount = self.subtotal * self.discount_percentage / 100
        self.discounted_amount = self.subtotal - self.discount

    def calculate_gst(self):
        self.gst = self.discounted_amount * self.gst_percentage / 100

    def calculate_final_bill(self):
        self.final_bill = self.discounted_amount + self.gst

    def display_bill(self):
        print("Product Name:", self.product_name)
        print("Subtotal:", self.subtotal)
        print("Discount:", self.discount)
        print("GST:", self.gst)
        print("Final Bill:", self.final_bill)


bill = ShoppingBill()
bill.attribute(input("Enter product name: "), float(input("Enter product price: ")),
               int(input("Enter quantity: ")), float(input("Enter discount percentage: ")),
               float(input("Enter GST percentage: ")))
bill.calculate_subtotal()
bill.calculate_discount()
bill.calculate_gst()
bill.calculate_final_bill()
bill.display_bill()
