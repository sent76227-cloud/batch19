'''
Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''


print("An employee wants to calculate salary per day and per hour.")
monthly_salary = int(input("Monthly Salary = "))
working_days = int(input("Working days = "))
working_hours = int(input("Working hours per day = "))


salary_per_day = monthly_salary/working_days
salary_per_hour = salary_per_day/working_hours


print(f"Salary per day = {salary_per_day}\nSalary per hour = {salary_per_hour}")