''' **9. Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even '''

n = int(input("Enter a digit: "))
count = 0
i = 1
even = 0
num = 0
while n > 0:
   a = n%10
   if a%2 == 0:
       even = even+1
   num = num+1
   n = n//10
if num == even:
   print("All no. is even")
else:
   print("Not all no. is even")
