'''3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3

---'''
l = list(map(int,input("Enter List: ").split()))
new  = []
for i in range(1,len(l)+2):
    new.append(i)



for i in range(len(new)):
    if new[i] not in l:
        print("Missing number: ",new[i])
        break