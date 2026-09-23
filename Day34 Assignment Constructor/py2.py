'''
Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0
'''
class cosutmer:
    def __init__(self,customer_id,customer_name,units_consumed):
        
        self.customer_id =     customer_id
        self.customer_name = customer_name
        self.units_consumer = units_consumed
    def calculation(self):
        cost = 8
        fixed_charge = 150
        self.total_bill = (self.units_consumer * cost) + fixed_charge
    def display(self):
        print("coustomer Id",self.customer_id)
        print("Coustomer name: ",self.customer_name)
        print("Units consumed: ",self.units_consumer)
        print("Total bill  ₹",self.total_bill)
        
        
        




customer_id = int(input("Enter id: "))
customer_name = input("Enter name: ")
units_consumed = int(input("Enter unit consumed: "))
uni1 = cosutmer(customer_id,customer_name,units_consumed)
uni1.calculation()
uni1.display()