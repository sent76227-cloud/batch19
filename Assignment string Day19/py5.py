''' 5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website '''

web = input("Enter Website: ")
pre = "www."
suff = ".com"
match = False
math = False
a = 0
i = 0
while i<=3:
     if pre[i] == web[i] :
        match = True
     else:
        match = False
     i = i+1


if web.endswith(suff):
    math = True
else :
    math = False          



if match == True and math == True :
     print("Valid Website.")
else:
    print("Invalide website: ")
           

     
       


