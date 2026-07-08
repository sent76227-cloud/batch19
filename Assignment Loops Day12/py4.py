'''
4.Unique Digit Security Scanner


A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept


Input:

57294


Output:

Valid Unique Code

'''
num = int(input("Enter a number"))

status = True
x = 1
while num>0:
   dig1 = num%10
   num = num//10
   while num > 0:
       dig2 = num%10
       if dig1 == dig2:
          print("Reject")
          x = 0
          break
       num = num//10
    
   else:
      print("Valid unique code")
   if x == 0:
      break
       

















'''

n=int(input("Enter number"))
unique=True
for i in range(1,len(str(n))+1):
    digit1=n%10
    n=n//10
    temp=n
    for i in range(1,len(str(temp))+1):
       digit2=temp%10
       temp=temp//10
       if digit1==digit2:
          print("Not valid")
          unique=False
          break
    if unique==False:
       break
else:
   print("Valid unique code")

'''
        
   
 
 
   
