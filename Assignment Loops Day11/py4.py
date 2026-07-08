
      

'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31 '''


num = int(input("Enter a number: "))



for i in range(2,num):
   if num%i==0:
       op = "not prime"
       print(op,"number")
       break
else:
   op = "prime"
   print(op,"number")

if op == "not prime":
   status1 = True
   while status1:
       num = num-1
       for i in range(2,num):
           temp = num
           if num%i==0:
              break
       else:
               print("Previous Prime number",temp)
               status1 = False
else:
   if op == "prime":
       status1 = True
       while status1:
           num = num+1
           for i in range(2,num):
               temp2 = num
               if num%i==0:
                 break
           else:
               print("Next Prime number",temp2)
               status1 = False

               
                 
   
       






