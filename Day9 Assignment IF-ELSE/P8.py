'''1. Smart Credit Card Approval System

A bank evaluates credit card applications based on income, credit score, employment type, and existing debt.

If income is greater than or equal to 50000, then check credit score. If credit score is greater than or equal to 750, then check debt. If debt is less than 20000, approve Premium Card; otherwise approve Gold Card. If credit score is less than 750, then check employment type. If employment is government and credit score is at least 650, approve Gold Card; otherwise reject.

If income is less than 50000, then check if income is at least 30000 and credit score is at least 700. If yes, approve Silver Card; otherwise reject.

Input:
Income = 45000
Credit Score = 720
Employment = private
Debt = 10000

Output:
Card Type = Silver Card'''

income = int(input("Enter Income: "))
credit = int(input("Enter credit score: "))
employment = input("Enter Employment type(private/government): ").lower()
debt = int(input("Enter Debt: "))

if income>=50000:
   if credit>=750:
      if debt<20000:
         print("Premium card")
      else:
         print("Gold card")
   else:
      if employment=="government":
         if credit>=650:
            print("Gold Card")
         else:
            print("Reject")
else:
   if income>=30000:
      if credit>=700:
         print("Silver card")
      else:
         print("reject")
