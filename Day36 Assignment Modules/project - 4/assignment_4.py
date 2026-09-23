from models.account import Account

accounts = [
    Account(101, "Amit", 45000),
    Account(102, "Rahul", 75000),
    Account(103, "Priya", 35000),
    Account(104, "Neha", 90000),
    Account(105, "Rohit", 55000),
]

print("All Accounts:")
for acc in accounts:
    acc.display()

print("\nSearch Account Number: 101")
account_found = None
for acc in accounts:
    if acc.account_no == 101:
        account_found = acc
        break
if account_found:
    account_found.display()

print("\nDeposit into Account 101")
for acc in accounts:
    if acc.account_no == 101:
        acc.deposit(10000)
        break
print("After Deposit:")
for acc in accounts:
    if acc.account_no == 101:
        acc.display()

print("\nWithdraw from Account 103")
for acc in accounts:
    if acc.account_no == 103:
        acc.withdraw(5000)
        break
print("After Withdrawal:")
for acc in accounts:
    if acc.account_no == 103:
        acc.display()

print("\nAccounts having balance greater than 50000:")
for acc in accounts:
    if acc.balance > 50000:
        acc.display()

highest = max(accounts, key=lambda acc: acc.balance)
print("\nHighest Balance Account:")
highest.display()
