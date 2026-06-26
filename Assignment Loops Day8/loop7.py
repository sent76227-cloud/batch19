''' 7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32   '''

num = int(input("enter n"))
dig = int(input("enter digi"))
power = 1
n = num
for i in range(1,dig):
   num = num * n
      
print(num)
      












