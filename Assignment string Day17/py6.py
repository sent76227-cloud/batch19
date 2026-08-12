'''
Railway Ticket PNR Analyzer
A railway department wants to verify whether a PNR number is valid.
Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
'''
passw = input("Enter PNR number: ")
p = 0
n = 0
r = 0
digit = 0
space = 1
special = 1

length = len(passw)
if length == 12:  
  i = 0
  while i < length:
     ch = passw[i]
     if i == 0:
        if "P" == passw[0] :
          p = 1
        else:
             print("Please write P in captial, and retry thank you ")
             break

        
     elif i == 1:
         if "N"==passw[1]:
             n = 1
         else:
              print("Please write N in captial, and retry thank you ")
              break

     elif i == 2:
          if "R" == passw[2]:
              r = 1
          else:
              print("Please write N in captial, and retry thank you ")
              break
     elif ch.isdigit():
            digit = digit+1
     elif ch == " ":
           space = 0
           print("Don't use space in PNR number")
           break 
     else:
         special = 0
         print("Not allowed to use special charaters and alphabates")     
 
     i = i+1
 
  
  if n == 1 and r == 1 and space == 1 and digit == 9 and special == 1:
       print("Valid PNR number")
  else:
        print("Invalid PNR Number please try again ")  
else:
  print("Length is not correct: ") 
  
   
'''pnr = input("Enter PNR Number: ")

if len(pnr) != 12:
    print("Invalid Length")

elif pnr[:3] != "PNR":
    print("PNR should start with PNR")

else:
    digit = 0
    valid = True

    for i in range(3, 12):
        if pnr[i].isdigit():
            digit += 1
        else:
            valid = False
            break

    if valid and digit == 9:
        print("Valid PNR Number")
    else:
        print("Invalid PNR Number")'''