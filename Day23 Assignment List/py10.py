'''====================================================================
10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found

---'''
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
    if 1 < count:
        
        elem.append(uniqe[i])
elem.sort()

if elem == []:
    print("No duplicate number")
else:
    print("Duplicate numbers: ",elem)
    print("Count ",len(elem))