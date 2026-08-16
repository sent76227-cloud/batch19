'''====================================================================
7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]

---
'''

arr = list(map(int, input("Enter array: ").split()))
n = len(arr)
k = int(input("Enter K: "))

for i in range(k):
    last = arr[-1]

    for j in range(n - 1, 0, -1):
        arr[j] = arr[j - 1]

    arr[0] = last

print(arr)