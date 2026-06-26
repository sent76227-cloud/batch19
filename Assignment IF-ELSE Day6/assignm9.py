''' 9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible '''

attendance = int(input("Enter attendance % : "))

if attendance >= 75 :
   print("Status: Eligible")

elif attendance >= 60 and attendance <= 74:
   print("Status: Eligible With warning")

else:
   print("Status: Not elgible")
  