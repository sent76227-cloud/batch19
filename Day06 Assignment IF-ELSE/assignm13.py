'''
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600 '''

salary = int(input("Enter salary: "))
rating = int(input("Enter rating: "))

if rating == 5:
   if salary < 20000:
       hike = salary + 2000 + salary*25//100
       print(hike)
   else:
       hike = salary + salary*25//100
       print(hike)

elif rating == 4:
   if salary < 20000:
       hike = salary + 2000 + salary*20//100
       print(hike)
   else:
       hike = salary+ salary*20//100
       print(hike)
       

elif rating == 3:
   hike = salary + salary*10//100
   print(hike)

elif rating == 2:
   hike =salary + salary*5//100
   print(hike)

else: 
   print("No hike")