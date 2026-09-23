class Account:
    def __init__(self, account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        elif amount > self.balance:
            print("Insufficient balance.")
        return self.balance

    def display(self):
        print(f"{self.account_no} {self.customer_name} {self.balance}")
