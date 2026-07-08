
'''
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime '''

num = int(input("Enter a number"))

count = 0
sum = 0
min = 9

while num > 0:
   dig = num%10
   sum = dig+sum
   if dig == 0:
       count = count + 1
   if dig < min:
      min = dig
      
   num = num//10
three_add = count + sum + min
mul = min*three_add
print("Zero count ",count)
print("sum =  ",sum)
print("Smallest digit = ",min)
print("zero count and sum = ", three_add)
print("Final Result = ",mul)
if mul == 0 or mul == 1:
   print("Not prime")
else:
   for i in range(2,mul):
       print(mul)
       if mul%i == 0 :
           print("Not Prime")
           break
   else:
       print("Prime number")


