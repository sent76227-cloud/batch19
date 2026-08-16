'''1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)
'''
k = int(input("Enter the value of k:"))
l = list(map(int,input("Enter list of: ").split()))
l.sort()
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]-l[i] == k:
            print("(",l[i],",",l[j],")")