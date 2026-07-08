''' 3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47 '''


a = int(input("Enter a num a: "))
b = int(input("Enter a num b: "))
print("Prime number's are: ")

for n in range(a,b+1):
   temp =  n
   for i in range(2,temp):
      if temp%i==0:
          break
   else:
      print(temp)

         
   








