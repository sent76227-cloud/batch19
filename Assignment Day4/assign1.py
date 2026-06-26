'''
Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
'''
print("You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.")

mobile_price = int(input("Enter Mobile Price: "))
down_payment =  int(input("Enter Down Payment: "))
inter_rate = int(input("Enter Interest rate: "))
total_month = int(input("Enter Months: "))
remaining_am = mobile_price - down_payment
total_int = remaining_am*10/100
total_amount = total_int + remaining_am
montly_emi = total_amount/total_month
print(f"Remaining Amount = {remaining_am}\nTotal With Interest = {total_amount}\Monthly EMI = {montly_emi}")
