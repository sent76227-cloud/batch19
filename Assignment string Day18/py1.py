''' 1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username '''

username = input("Enter username: ")


length = len(username)
allp = 0
leter = 0
digit = 0
underscore = 0
space = 1
special = 1
if length >= 5 and length <= 12:
  i = 0
  while i < length:
    ch = username[i]
    if i == 0:
        if ch.isalpha():
            allp = 1
        else:
          print("first letter of the username must start with letter")
    elif ch.isalpha():
          leter = 1
    elif ch.isdigit():
         digit = 1
    elif ch == "_":
         underscore = 1
    elif ch == " ":
        space  = 0
    else:
        special = 0
    i = i+1
  if allp == 1 and leter == 1 and digit == 1 and underscore == 1 and space == 1 and special == 1:
        print("The Username is Right : ")
  else:
         print("Retry!!  ")





else:
  print("Length of the username is invalid! ")