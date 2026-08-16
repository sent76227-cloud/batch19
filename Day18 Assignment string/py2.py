''' 
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12 '''

num = input("Enter contact number : ")


length = len(num )
allp = 0
digit=0
space = 1
special = 1

i = 0
while i < length:
    ch = num [i]
    if ch.isalpha():
       allp = 1
       break
    elif ch.isdigit():
       digit = digit+1
    elif ch == " ":
          space = 0
    else:
        special = 0       
    i = i+1
if allp == 1 and space  == 1 and special == 1:            
    print("invalid input : ")
else:
   print("Total digits: ",digit)
  