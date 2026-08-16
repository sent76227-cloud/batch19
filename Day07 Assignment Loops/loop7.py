''' **7. Count Even Digits**
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to **count the number of even digits in a given number using loops**.

Input: 123456
Output: Even digits count = 3 '''

n = int(input("Enter a digit: "))
count = 0
i = 1
while n > 0:
   a = n%10
   if a%2 == 0:
       count = count+1
   n = n//10
print(f"Even digits count = {count}")
    

