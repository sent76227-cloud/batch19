''' 7.
Neon Number Detector

Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:
1
9 '''


a = int(input("enter a "))
b = int(input("enter b "))



for n in range(a,b+1):
   temp = n
   squ = temp*temp
   sum = 0
   length = len(str(squ))
   for i in range(1,length+1):
      dig = squ%10
      sum = dig+sum
      squ = squ//10
   if sum == n:
        print(sum)
      




















