''' 14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor '''



n1 = int(input("Enter N1 number: "))
n2 = int(input("Enter N2 number: "))
num = 0

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