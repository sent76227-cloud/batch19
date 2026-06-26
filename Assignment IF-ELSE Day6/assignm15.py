'''
 15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220 '''

vehicle = input("enter vehicle type:").lower()
hours = int(input("Enter hours: "))

if vehicle == "bike":
   if hours > 5:
       fee = hours * 10
       fee = fee+100
       print(fee)
   else:
       fee = hours * 10
       print(fee)
elif vehicle ==  "car" :
   if hours > 5:
       fee = hours * 20
       fee = fee+100
       print(fee)
   else:
       fee = hours * 20
       print(fee)
elif vehicle ==  "bus":
   if hours > 5:
       fee = hours * 50
       fee = fee+100
       print(fee)
   else:
       fee = hours * 10
       print(fee)

       