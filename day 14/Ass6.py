'''
6.
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
191
'''
start=int(input("Enter Starting number: "))
end=int(input("Enter ending number: "))
for i in range(start,end+1):
   rev=0
   n=i
   while n>0:
     digit=n%10
     rev=rev*10+digit
     n=n//10
   if rev==i:
      print(i,end=" ")
