''' 
Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
'''
daily_wage = int(input("Enter Daily wage: "))
days =  int(input("Enter Days: "))
salary = int(daily_wage*days)
print(f"Salary = {salary} ")
