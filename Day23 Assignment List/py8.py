'''8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found

---
'''
l = list(map(int,input("Enter list: ").split()))
uniqe = []
for i in l:
    if i not in uniqe:
        uniqe.append(i)
max = 0
elem  = []
for i in range(len(uniqe)):
    count = 0
    
    for j in range(len(l)):
        if l[j] == uniqe[i]:
            count = count+1
    if max < count:
        max = count
        elem.append(uniqe[i])

print("Maximum Repeated Element is ",elem[len(elem)-1],"is repeat",max,"times")