'''1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ********9012'''



acc = input("Enter account number: ")
rev = ""
a = "*"
i = 0
while i<len(acc):
       if i > len(acc)-5:
          rev = rev+acc[i]
       else:
          rev = rev+a
       i = i+1
print("Masked Account: ",rev)
       


