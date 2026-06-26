''' 3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5'''

num = int(input("Enter a number: "))
rev = 0 

i = 1
while num > 0 :
   temp = num%10
   rev =  rev*10+temp
   num = num//10

last = rev%10
print(last)






















''' 
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2 

num = int(input("Enter a number: "))
min = 9



i = 1
while num > 0 :
   check = num%10
   if min > check:
       min = check
   num = num//10

print("Minimum no. is : ",min) '''




























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


