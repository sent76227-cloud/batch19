'''
5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
'''
username = input("Enter username: ")
passw =   input("Enter password: ")
length = len(passw)

if username == "admin":
    print("Valid User")
if length >=8 :
    print("Password is strong")