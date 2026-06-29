'''7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number '''

num = int(input("Enter a number: "))

i = 1
x = 0
while num > 0:
   dig = num%10
   if dig == 0:
       x = 1
       break
   num = num//10
if x == 1:
   print("Number is  duck")
else:
   print("Number  is not duck")


'''
else:
   print("Is not duck number")
   

print("Duck number")'''
   
         
  

           
           
   


