'''4.
Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password'''
def password(digit):
    if digit == 0:
        return 0
    last = digit%10
    if last%2==0:
        return 1 + password(digit//10)
    else:
        return 0
digit = int(input("Enter digit here"))
check=(password(digit))

if len(str(digit)) == check:
    print("Strong password")
else:
    print("weak password")