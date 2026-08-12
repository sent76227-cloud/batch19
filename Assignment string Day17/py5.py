'''

5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45
Output: Secure Password
 '''

passw = input("Enter password: ")

length = len(passw)
captial = 0
digit = 0
lower = 0
special = 0
last = 0
space = 1
if length >= 8:  
  i = 0
  while i < length:
     ch = passw[i]
     if i == 0:
        if "A" <= passw[0] and "Z" >= passw[0]:
          captial = 1
        else:
            break
     else:

       if i == length-1 or i == length:
            if ch.isdigit():
             last = last+1
             


          
       elif ch.isdigit():
          digit = digit+1
       elif ch == " " :
           space = 0
           break
       elif ch >= "a" and ch<="z":
           lower = 1
       
       else:
           special = 1
         
          
     
 
     
     i = i+1
  
  if captial  == 1 and digit>=2 and space == 1 and lower == 1 and special == 1  and last == 2:
       print("Valid password")
  else:
        print("Invalid password please try again")   
print("Out of the loop ")   
   
 