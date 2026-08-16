'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000 '''

course = input("Enter course category: ").lower()
user_type = input("Enter user type: ").lower()


# Programming → ₹5000
# Design → ₹4000
# Marketing → ₹3000


if course == "programming":
   if user_type == "student":
       dis = 5000-(5000*20//100)
       print("Final Course Fee: ₹",dis)
   elif user_type == "working professional":
       dis = 5000-(5000*10//100)
       print("Final Course Fee: ₹",dis)
   else:
       print("No discount")

elif course == "design":
   if user_type == "student":
       dis = 4000-(4000*20//100)
       print("Final Course Fee: ₹",dis)
   elif user_type == "working professional":
       dis = 4000-(4000*10//100)
       print("Final Course Fee: ₹",dis)
   else:
       print("No discount")

else:
   if course == "marketing":
       if user_type == "student":
           dis = 4000-(3000*20//100)
           print("Final Course Fee: ₹",dis)
       elif user_type == "working professional":
           dis = 3000-(3000*10//100)
           print("Final Course Fee: ₹",dis)
   else:
       print("No discount")

       