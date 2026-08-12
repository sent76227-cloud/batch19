'''5.
Given an unsorted array arr[] of size N having both negative and positive integers.
The task is place all negative element at the end of array without changing the order of positive element and negative element.

Example 1:
Input :
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output :
1  3  2  11  6  -1  -7  -5

Example 2:
Input :
N=8
arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output :
7  9  10  11  -5  -3  -4  -1
'''
size = int(input("Enter size of list: "))


while True:
    arr = list(map(int,input("Enter list: ").split()))
    if len(arr) == size:
        break
    else:
        print("enter Size ==  length of list")
        break
print(arr)
poss = []
nega = []
for i in arr:
    if 0<=i:
        poss.append(i)
    else:
        nega.append(i)
poss.extend(nega)
print(poss)