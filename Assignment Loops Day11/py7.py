'''7.Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number ''' 


num = int(input("Enter a num: "))
length = len(str(num))

sum = 0

for i in range(1,length+1):
   dig = num%10
   sum = sum+dig
   num = num//10

print("Sum =",sum)
if sum == 0 or sum == 1:
   print("Not prime")
else:
   for i in range(2,sum):
       if sum%i == 0 :
           print("Normal")
           break
   else:
       print("Lucky Number")





