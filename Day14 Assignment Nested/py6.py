''' 6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191 '''



a = int(input("enter a "))
b = int(input("enter b "))



for n in range(a,b+1):
   temp = n
   rev = 0
   length = len(str(temp))
   for i in range(1,length+1):
       dig = temp%10
       rev = rev*10+dig
       temp = temp//10
   if rev == n:
       print(rev)







