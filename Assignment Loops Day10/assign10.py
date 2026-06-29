''' 10.
 Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number '''

num = int(input("Enter a number"))
count = 0

for i in range(1,num):
   if num%i == 0:
       count = count+1
if count <= 2:
   print("Prime number")
else:
   print("composite number")
       
            
         
  

           
           
   


