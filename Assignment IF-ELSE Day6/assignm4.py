'''
4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050
'''
purchase_amount = int(input("Enter purchase amount: "))

if purchase_amount >= 5000:
   dis = purchase_amount - (purchase_amount*20//100)
   print("Final Amount: ₹:",dis)
elif purchase_amount >= 2000 and purchase_amount <= 5000 :
   dis = purchase_amount - (purchase_amount*10//100)
   print("Final Amount: ₹",dis)
else:
   dis = purchase_amount - (purchase_amount*5//100)
   print("Final Amount: ₹",dis)