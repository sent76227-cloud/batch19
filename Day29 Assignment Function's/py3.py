'''
3.
ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System.
 The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements

Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information

* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1

Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---

Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully

---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully

---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000

---

Enter Choice : 5

Customer Profile Displayed Successfully

---

Enter Choice : 6

Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.

Note:
Marks will be awarded based on the correct usage of the specified argument type in each menu option.'''

def customerregistration(name, email, mobile):
    print("Customer Name :", name)
    print("Email :", email)
    print("Mobile :", mobile)
    print("Customer Registered Successfully.")


def productinformation(productname, price, category):
    print("Product Name :", productname)
    print("Price :", price)
    print("Category :", category)
    print("Product Details Displayed Successfully.")


def generateinvoice(productname, price, tax=18):
    taxamount = price * tax / 100
    finalamount = price + taxamount

    print("Product Name :", productname)
    print("Price :", price)
    print("Tax :", tax, "%")
    print("Final Amount :", finalamount)
    print("Invoice Generated Successfully.")


def addproducts(*prices):
    total = 0

    for price in prices:
        total = total + price

    return total


def customerprofile(**details):
    for key, value in details.items():
        print(key, ":", value)


while True:
    print("******** ONLINE SHOPPING SYSTEM ********")
    print("1. Customer Registration")
    print("2. Product Information")
    print("3. Generate Invoice")
    print("4. Add Multiple Products")
    print("5. Display Customer Profile")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            mobile = input("Enter Mobile: ")

            customerregistration(name, email, mobile)

        case 2:
            productname = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            category = input("Enter Category: ")

            productinformation(
                productname=productname,
                price=price,
                category=category
            )

        case 3:
            productname = input("Enter Product Name: ")
            price = float(input("Enter Price: "))

            generateinvoice(productname, price)

        case 4:
            n = int(input("Enter Number of Products: "))

            prices = []

            for i in range(n):
                price = float(input("Enter Price " + str(i + 1) + ": "))
                prices.append(price)

            total = addproducts(*prices)

            print("Total Bill Amount :", total)

        case 5:
            name = input("Enter Name: ")
            city = input("Enter City: ")
            email = input("Enter Email: ")
            mobile = input("Enter Mobile: ")
            membership = input("Enter Membership Type: ")

            customerprofile(
                Name=name,
                City=city,
                Email=email,
                Mobile=mobile,
                Membership=membership
            )

        case 6:
            print("Thank You. Program Terminated.")
            break

        case _:
            print("You entered a wrong choice.")

