''' **13. Number Range Display System (if-elif with loops)**
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using **if-elif-else and loops** to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same '''


n1 = int(input("Enter N1 number: "))
n2 = int(input("Enter N2 number: "))

if n1 < n2:
   for i in range(n1,n2+1):
       print(i,end = " ")
elif n1 > n2:
   for i in range(n1,n2,-1):
       print(i,end = " ")
      
       
else:
   if( n1 == n2):
       print("both no. are same ")








'''n = int(input("Enter a digit: "))
count = 0
score = 1
num = 0
i = 1
while n > 0:
   a = n%10
   score = a*score
   n = n//10
print(score)
if score%2 == 0:
   print("Even")
else:
   print("Odd")'''