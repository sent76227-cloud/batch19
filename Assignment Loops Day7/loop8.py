''' **8. Count Odd Digits**
A banking system flags IDs with too many odd digits for further verification.
Write a program to **count the number of odd digits in a given number using loops**.

Input: 123456
Output: Odd digits count = 3 '''



n = int(input("Enter a digit: "))
count = 0
i = 1
while n > 0:
   a = n%10
   if a%2 != 0:
       count = count+1
   n = n//10
print(f"Odd digits count = {count}")
    

