''' 
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2 '''

num = int(input("Enter a number: "))
min = 9



i = 1
while num > 0 :
   check = num%10
   if min > check:
       min = check
   num = num//10

print("Minimum no. is : ",min)




























'''num = int(input("Enter a number: "))
check = 0
max = 0 
i = 1
min = 0
while num > 0 :
   max = num%10
   if max < min:
      min = max
print("Smallest no. ",min)
num = int(input("Enter a number: "))
check = 0
mix = 9 
leng = len(str(num))
for i in range(0,leng):
   check = num%10
   if min > check:
       min = check
   num = num//10
print(min) '''


