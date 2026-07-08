'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime '''


num = int(input("Enter a num"))
length = len(str(num))

lar = 0
small = 9
for i in range(1,length+1):
   dig = num%10
   if lar<dig:
     lar = dig
   if dig < small:
     small = dig
   num = num//10
print("largest : ",lar)
print("smallest : ",small)
sum = lar + small
print("Sum : ",sum)


if sum == 0 or sum == 1:
   print("Not prime")
else:
   for i in range(2,sum):
       if sum%i == 0 :
           print("Not Prime")
           break
   else:
       print("Prime number")