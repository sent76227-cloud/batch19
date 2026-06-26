'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to **check whether a number is an Armstrong number using loops**.

Input: 153
Output: Armstrong '''
n = int(input("Enter a number"))
temp = n
sum = 0
for i in range(1,4):
   a = n%10
   mul = a*a*a
   sum = sum+mul
   n = n//10
print(sum)


   