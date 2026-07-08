''' 
3.

 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

--- '''




x = 0
while True:
   print("Menu Options: ")
   print("1.Deposit Money")
   print("2.Withdraw Money")
   print("3.Check Balance")
   print("4.Apply Interest")
   print("5.Exit")
   selct = int(input("Select any one option form this: "))
     
   match selct:
       case 1:
             if x == 0:
               depo = int(input("Deposit Money: "))
               print("Amount",depo)
               x = 1
               continue
       case 2:
             if x == 1:
               withdrawl = int(input("Enter amout of withdrawl"))
               if withdrawl <= depo:
                     print("With drawl Successfull: ",withdrawl)
               else:
                  if withdral >=depo:
                   print("Insufficinet amount")
                  else:
                    if depo == 0:
                         print("No balance available. Please deposit firt")
                    else:
                        print("The wrong input noted")
                           
            
       case 3:
           if x == 1:
             depo = depo - withdrawl
             print("Cureent balance: ",depo)
         
              
           else:
              print("please deposite money first")  
       case 4:
           if x == 1:
               if depo > 50000:
                    int = depo*5//100
                    sumint = int+depo
                    print("Intrest : ",int)
                    print("With Intrest: ",sumint)
               else:
                    int = depo*3//100
                    sumint = int+depo
                    print("Intrest : ",int)
                    print("With Intrest: ",sumint)
                   

           else:
              print("Please deposite money first") 
       case 5:
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