'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime '''









num = int(input("Enter a num"))
length = len(str(num))
even = 0
odd = 0
for i in range(1,length+1):
   dig = num%10
   if dig%2==0:
     even = even+1
   else:
     odd = odd + 1
   num = num//10
print("even count ",even)
print("odd count",odd)
diff = abs(even - odd)
print("differece",diff)

if diff == 0 or diff == 1:
   print("Not prime")
else:
   for i in range(2,diff):
       if diff%i == 0 :
           print("Not Prime")
           break
   else:
       print("Prime number")
   