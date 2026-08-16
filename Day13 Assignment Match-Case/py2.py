
''' 

2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

--- 
Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!

'''

'''
x = 0
while True:
   print("Menu Options: ")
   print("1.Enter Basic Salary")
   print("2.Calculate HRA(20%) and DA (10%)")
   print("3.Calculate Net Salary")
   print("4.Tax Deduction")
   print("5.Display Salary Slip")
   print("6.Exit")
   selct = int(input("Select any one option form this: "))
     
   match selct:
       case 1:
             if x == 0:
               salary = int(input("Enter salary: "))
               print("Basic Salary",salary)
               x = 1
               continue
       case 2:
             if x == 1:
               HRA = salary*20//100
               DA = salary*10//100 
               print("HRA",HRA)
               print("DA",DA)
             else:
                print("please enter basic salary first")
       case 3:
           if x == 1:
              HRA = salary*20//100
              DA = salary*10//100
              sum = HRA+DA+salary
              print("Net salary",sum)
              
           else:
              print("please enter basic salary first")  
       case 4:
           if x == 1:
       
              HRA = salary*20//100
              DA = salary*10//100
              sum = HRA+DA+salary
              taxper = sum*10//100
              aftax = sum - taxper
              print("After Tax salary",aftax)
           else:
              print("please enter basic salary first") 
       case 5:
           if x == 1:
              HRA = salary*20//100
              DA = salary*10//100
              sum = HRA+DA+salary
              taxper = sum*10//100
              aftax = sum - taxper

              print("Basic salary",salary)
              print("HRA",HRA)
              print("DA",DA)
              print("Net salary",sum)
              print("Final Salary",aftax)
           else:
              print("please enter basic salary first")
       case 6:
             break
             x = 0
   con = input("Do you want continue yes/no").lower()
   if con == "yes":
      continue
   elif con == "no":
       break
   else:
       print("Please enter ryt input")
              

print("Thank youu have a nice day: ")

'''         
              
   




num1= int(input("Enter num1"))
num2= int(input("Enter num2"))

for i in range(num1,num2):
    a=num1
    x = True
    for i in range(2,num2):
        if a%i==0:
           #print("Not prime")
           x =  False
           break
    if x == True:
        print(a)




































'''
while True:
   print("Menu Options: ")
   print("1.Prime Number")
   print("2.Palindrome Number")
   print("3.Reverse a Number")
   print("4.Count Digits")
   print("5.Exit")
   option = int(input("Choice the follwoing option"))
   match option:
         case 1 :
                num = int(input("To find the prime number"))
                for i in range(2,num//2+1):
                       if num%i==0:
                           print("Not a prime number")
                           break
                else:
                     print("Prime number")
         case 2 :
               num = int(input("To find the Palindrome"))
               temp = num
               rev = 0
               while num > 0:
                    dig =  num%10
                    rev = rev*10+dig
                    num = num//10
               if rev == temp:
                   print("Number is palindrome: ")
               else:
                   print("Number is not palindrome")
         case 3 :
               num = int(input("Reverse"))
               rev = 0
               while num > 0:
                    dig =  num%10
                    rev = rev*10+dig
                    num = num//10
               print(rev)
         case 4 :
               num = int(input("Cont the Digit"))
               count = 0
               while num > 0:
                  count = count+1
                  num = num//10
         case 5 :
               print("Existing the programe, Thank you!!!")
               break
   reop = input("Do you want to continoue yes/no").lower()
   if reop == "yes":
              continue
   elif reop == "no":
             break
   else:
           print("you enter wrong input")
  '''






