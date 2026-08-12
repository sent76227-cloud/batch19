'''
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''
number = input("Enter Vehicle Number: ")
allp = 0

digit = 0
space = 1
special = 1

length = len(number)
if length == 10:  
  i = 0
  while i < length:
     ch = number[i]
     if i == 0 or i == 1 or i == 4 or i == 5:
        if ch.isalpha():
          allp = allp+1
        else:
             print("Please write first letter alphabate only ")
             break
     elif ch.isdigit():
         digit = digit+1 

     else:
         special = 0
         print("Not allowed to use special charaters and extra alphabates")     
 
     i = i+1
 
  
  if allp == 4 and digit == 6 and special == 1 :
       print("Valid Vehicle number")
  else:
        print("Invalid vehicle  Number. please try again ")  
else:
  print("Length is not correct: ") 
  
   
 