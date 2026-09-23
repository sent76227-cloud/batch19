'''QNO 1: Bank Account Management System

ABC Bank wants to develop a software application to manage customer accounts.

Each customer has:

Account Number
Customer Name
Account Balance

A customer should be able to:

Deposit money
Withdraw money
Check account balance
Transfer money to another customer

The bank also wants to maintain information that is common for all customers:

Bank Name
Interest Rate

The bank management may change the interest rate in the future, and the change should apply to all customers.

Additionally, the application should provide some utility operations:

Validate whether an account number is valid.
Calculate interest on a given amount.
Generate a transaction ID.
Requirements

Class Variables

bank_name
interest_rate

Instance Variables

account_no
customer_name
balance

Instance Methods

deposit(amount)
withdraw(amount)
transfer_money(receiver, amount)
display_balance()

Class Methods

change_interest_rate(new_rate)
change_bank_name(new_name)
display_bank_info()

Static Methods

validate_account_number(account_no)
calculate_interest(amount, rate)
generate_transaction_id()

Sample Input
Customer 1
Account No : 1001
Name       : deepika
Balance    : 50000

Customer 2
Account No : 1002
Name       : Priya
Balance    : 30000

Deposit Amount : 10000
Transfer Amount : 15000
New Interest Rate : 7.5
Sample Output
Customer : deepika
Balance  : 45000

Customer : Priya
Balance  : 45000

Bank Name      : ABC Bank
Interest Rate  : 7.5%
Transaction ID : TXN1025

Task: Design a Python class named BankAccount and implement all the above methods using instance methods, class methods, and static methods appropriately.'''
class BankAccount:
    bank_name = "not define now"
    interest_rate = 0
    def __init__(self,account_no,coustomer_name,balance):
        self.account_no =account_no
        self.coustomer_name = coustomer_name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdraw(self,amount):
        self.balance = self.balance - amount
    def display_balance(self):
        print("Balance is ",self.balance)
    @classmethod
    def change_interest_rate(cls,interest_rate):
        cls.interest_rate = interest_rate
    @classmethod
    def change_bank_name(cls,new):
        cls.bank_name = new
    @classmethod
    def display(cls):
        print("Bank name: ",)
        print("Display interest rate: ",cls.change_interest_rate)
    @staticmethod
    def validat_account_number(account_no):
        if account_no >= 10:
            print("Validate")
        else:
            print("Not validate: ")
    @staticmethod
    def calculalte_interese(balance,intreset_rate):
        interest_caluculte =  balance*(intreset_rate/100)
    def generate_transaction_id():
        transaction_id = int(input("Enter transaction id"))
        print(transaction_id)

account_no = int(input("Enter account number: "))
coustomer_name =  input("Enter coustomer name: ")
balance =  int(input("Enter balance: "))
amount = int(input("Enter amount: "))
customer1 = BankAccount(account_no,coustomer_name,balance)
customer1.deposit()
customer1.withdraw()
customer1.display_balance()
BankAccount.change_bank_name("Axis")
BankAccount.change_interest_rate(5)
BankAccount.display()




        
        