'''
2. An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800
'''
cart_value = int(input("Enter Cart Value: "))
user_type = input("Enter User Type: ").lower()
dis20 = cart_value - (cart_value *20/100)
dis10 = cart_value - (cart_value *10/100)
dis5 = cart_value - (cart_value *5/100)
dis20 = int(dis20)
dis10 = int(dis10)
dis5 = int(dis5)
if cart_value >= 5000:
   if user_type == "premium":
       print(dis20)
   else:
       print(dis10)
else:
   if cart_value < 5000 and cart_value >= 2000:
       print(dis5)
   else:
       print("No discount applied")