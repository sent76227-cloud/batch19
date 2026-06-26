'''
5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome
'''

n = int(input("Enter a Number: "))
rev = 0
tem = n
while n > 0 :
   rev = rev*10+n%10
   n = n//10
if rev == tem:
   print("No. is palindrome")
else:
   print("No. is not palindrome")