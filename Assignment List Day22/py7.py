'''7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3'''

a = list(map(int,input("Enter list: ").split()))

new = []
for i in a:
    j = 1
    mul = 1
    while j <= i:
        mul = mul*j
        j = j+1
    new.append(mul)
print("New list : ",new)
sum = 0
max = -1
even = 0
for i in new:
    sum = sum+i
    if max<i:
        max = i
    if i%2==0:
        even = even+1
print("Sum:" , sum)
print("Max",max)
print("Even",even)
