'''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''
start=int(input("Enter Starting number: "))
end=int(input("Enter ending number: "))
for i in range(start,end+1):
   n=i
   l=len(str(n))
   sum=0
   while n>0:
     digit=n%10
     sum+=digit**l
     n=n//10
   if sum==i:
      print(i,end=" ")
    