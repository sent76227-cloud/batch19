'''Assignment 1 — Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days
 '''
from datetime import datetime,date,timedelta

dob =  input("enter bod (dd-mm-yyyy)")
db  =  datetime.strptime(dob,"%d-%m-%Y").date()
today = date.today()
print(db)
print(today)
age =  today.year - db.year
day = today -  db
print("Age ",age)
print("Days ",day.days)
nextbirthday = 
