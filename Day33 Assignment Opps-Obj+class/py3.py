'''Assignment 3: Bank Account Operations'''

class BankAccount:
    def attribute(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def display_account(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.holder_name)
        print("Final Balance:", self.balance)


account = BankAccount()
account.attribute(int(input("Enter account number: ")), input("Enter account holder name: "),
                  float(input("Enter opening balance: ")))
account.deposit(float(input("Enter deposit amount: ")))
account.withdraw(float(input("Enter withdrawal amount: ")))
account.display_account()
