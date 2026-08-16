'''6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0

'''

a = list(map(int,input("enter list element: ").split()))

prime = []

i = 0
while i < len(a):
        j = 2
        flag = 1
        while j < a[i]-1:
            if a[i]%j == 0:
                flag = 0
                break
            j = j+1
        
        if flag == 1:
            prime.append(a[i])
        i = i+1
print("Prime number is ",prime)
sum = 0
max = -1
count = 0
if 1 < len(prime):
    for i in prime:
        sum = sum+i
        if max < i:
            max = i
        count = count + 1
print("Sum ",sum)
print("Maximum: ",max)
print("Count:",count)
                
    