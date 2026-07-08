'''
3.Prime Number Range Checker

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
47'''
start=int(input("Enter Starting number: "))
end=int(input("Enter ending number: "))
for n in range(start,end+1):
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
       print(n)
