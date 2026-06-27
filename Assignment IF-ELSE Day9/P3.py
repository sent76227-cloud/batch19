'''6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged'''

trans = int(input("Enter Transaction amount: "))
location = input("Enter location(international/domestic): ").lower
age = int(input("Enter account age: "))
OTP = input("Enter OTP status(Verified/NOT): ").lower
unusual = input("Enter activity:(yes/no) ").lower

if trans>=10000:
   if location=="international":
      if OTP=="verified":
         print("Allow")
      else:
         print("Blocked")
   else:
      if trans>=50000:
         if age>=2:
            print("Allowed")
         else:
            print("Flagged")
      else:
         print("Allow")
else:
   if unusual=="yes":
      print("Flagged")
   else:
      print("Allow")
             