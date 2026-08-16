''' 
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number '''

num = int(input("Enter a number"))
length = len(str(num))
rev = 0

for i in range(1,length+1):
   dig = num%10
   rev = rev*10+dig
   num = num//10
num2 = rev
sum = 0
max = 1
temp = 0

length2 = len(str(num2))
for i in range(1,length2):
   dig1 = num2%10
   num2 = num2//10
   dig2 = num2%10
   diff = abs(dig1 - dig2)
   temp = temp*10+diff
   if max < diff:
       max = diff
   sum = sum+diff

print(temp.spilt" ")
lenght3 = len(str(temp))
for i in range(1,length3):
   di1 = temp%10
   if sum%di1:
       status = "Balanced: "
   temp =  temp//10

   





print(sum)
print(max)
print(status)
   
  


