'''

2.
Step Difference Number Analyzer(3.5 marks)

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

    
n = input("Enter number: ")


rev = ""
for x in range(0,len(n)):
    rev =  n[x] +rev


a = int(rev)
x = 0

print(a)
sum = 0
max = 0
for i in range(0,len(str(a))):
      dig = a%10
      
         
      a = a//10
      for x in range(1,len(str(a))):
          dig2 = a%10
          print("dig -",dig2)
      diff = abs(dig2 - dig)
      sum  = sum + diff
      if max < diff:
         max  = diff
     
    
      print(diff,end=" ")
print()
if x == 1:
  print("Balanced number")
else:
   print("Unbalanced Numb")
print("Sum",sum)
print("Max",max)


   







