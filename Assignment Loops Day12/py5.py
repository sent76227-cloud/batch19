'''
5.Number Stability Analyzer


A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number


Input:

12359


Output:

Stable Number
'''
n=int(input("Enter number: "))
stable=True
for i in range(1,len(str(n))+1):
    digit1=n%10
    n=n//10
    digit2=n%10
    temp=n
    if digit1<digit2:
      print("Not stable number")
      break
else:
   print("Stable number")

        
   
 
 
   
