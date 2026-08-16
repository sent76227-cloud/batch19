'''
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code '''


code = input("Enter product code: " )
length = len(code)
a = 0
count = 0

i = 0
while i < length//2:
   if code[i] == code[length-i-1]:
       count = count+1
  
  
   i = i+1
if length//2 == count:
    print("Palindrome Code ")
else:
   print("Not Palindrome Code")




             