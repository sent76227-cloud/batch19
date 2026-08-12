''' 
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''

emp = input("Enter Employe Id : ")


empcount = 0
digit = 0

length = len(emp)
if length == 8:
   i = 0
   while i<length:
         ch = emp[i]
         if i == 0 or i == 1 or i == 2:
           if ch == "E" and i == 0 :
                empcount = empcount+1
           elif ch == "M" and i == 1:
              empcount = empcount+1
           elif ch == "P" and i == 2:
             empcount = empcount+1
         elif ch.isdigit():
             digit = digit+1
         i = i+1
   if empcount == 3 and digit == 5:
            print("Valid Employee Id")
   else:
        print("Invalid Employee Id")  





             