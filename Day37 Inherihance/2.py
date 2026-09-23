
class Account:
    
    def __init__(self,account_number,customer_name,balance):
        self.account_number=account_number
        self.customer_name=customer_name
        self.balance=balance
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        if value<0:
            print("Balance cannot be negative.")
            self.__balance=0
            
        else:
            self.__balance=value
            
    @balance.deleter
    def balance(self):
        del self.__balance
    
        
    def display_account(self):
        print("\n Account Details")
        print("Account Number: ",self.account_number)
        print("Customer Name: ",self.customer_name)
        print("Balance: ",self.balance)
        
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
        else:
            print("Deposite amount must be positive.")
        
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance=self.balance-amount
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
       
        
class SavingAccount(Account):
    
    def __init__(self, account_number, customer_name, balance,interest_rate):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate=interest_rate
        
    def display_account(self):
            super().display_account()
            print("\nAccount Type: Saving Account")
            print("Interest Rate: ",self.interest_rate) 
                       
class PremiumSavingAccount(SavingAccount):
    
    def __init__(self, account_number, customer_name, balance, interest_rate,cashback_percentage):
        super().__init__(account_number, customer_name, balance,interest_rate)
        self.cashback_percentage=cashback_percentage
         
    def display_account(self):
            super().display_account()
            print("\nAccount Type: Premium Saving Account")
            print("Cashback Percentage: ",self.cashback_percentage)
              
account_number=int(input("Enter Account Number: "))
customer_name=input("Enter Customer Name: ")
initial_balance=float(input("Enter Initial Balance: "))

print("\n1. Saving Account")
print("2. Premium Saving Account")

account_type=int(input("Enter Account Type: "))

if account_type==1:
    interest_rate=float(input("Enter Interest Rate: "))
    account=SavingAccount(account_number,customer_name,initial_balance,interest_rate)
elif account_type==2:
    interest_rate=float(input("Enter Interest Rate: "))
    cashback_percentage=float(input("Enter Cashback Percentage: "))
    account=PremiumSavingAccount(account_number,customer_name,initial_balance,interest_rate,cashback_percentage)
else:
    print("Invalid Account Type: ")
    exit()

account.display_account()
    
deposit_amount = float(input("\nEnter amount to deposit: "))

account.deposit(deposit_amount)

print("\nAfter Deposit:")
print("Balance:", account.balance)

withdraw_amount = float(input("Enter amount to withdraw: "))

account.withdraw(withdraw_amount)

print("\nAfter Withdrawal:")
print("Balance:", account.balance)

