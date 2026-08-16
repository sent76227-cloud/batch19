''' 2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4 '''

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
count = 0
for i in range(1,num2+1):
   if i%7==0:
       count = count+1
       
print("Count = ",count)
   


       