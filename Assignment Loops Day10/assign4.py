''' 4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number ''' 
num = int(input("Enter a num"))
temp = num
sum = 0
length = len(str(num))
for i in range(1,length+1):
   dig = num%10
   fac = 1
   for i in range(dig,0,-1):
       fac = fac*i
   sum = sum + fac
   num = num//10
if sum == temp :
    print("Storng Number")
else:
   print("Try new number")




'''
i = 1
while num > 0:
   dig = num%10
   fac = dig * i
   print(fac,end = " ")
   sum = sum + fac
   num = num //10
print(sum)
'''



           
           
   


