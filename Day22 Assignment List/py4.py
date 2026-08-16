'''4.

Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

Definition

A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

An element is called a leader if:

It is greater than all elements to its right side
The element must be valid, i.e., it should not be:
Negative number
Zero

Rightmost valid element is always considered a leader.

Input Format
First line → integer n
Second line → n space-separated integers

Output Format
Single integer → sum of all valid leader elements
If no valid elements exist → return -1

Rules
Before finding leaders:

Ignore all negative values and zeros
Work only on positive numbers
Then find leaders from the filtered sequence

Test Case 1

Input:
8
16 0 17 4 -3 3 5 2

Processing:
Filtered array:
[16, 17, 4, 3, 5, 2]

Leaders:
[17, 5, 2]

Output:
24

Test Case 2

Input:
6
-1 0 -5 0 -2 -3

Output:
-1

Test Case 3

Input:
5
10 20 30 40 50

Processing:
Filtered array:
[10, 20, 30, 40, 50]

Leaders:
[50]

Output:
50
'''
size = int(input("Enter size of list: "))
arr = []
for i in range(size):
    arr.append(int(input("enter value:")))

    
#itrate to remove nagative 
a = []
for i in arr:
    if 1<=i:
        a.append(i)
print(a)


new = []
peakvalue = -1
for i in range(len(a)):
    if i == 0:
        if len(a) == 1:
            new.append(a[i])
            break
        if len(a) == 1:
            new.append(a[i])
            break
        elif a[i+1] < a[i]:
            new.append(a[i])
    elif i == len(a)-1:
        if a[i-1] < a[i] or i == len(a)-1:
            new.append(a[i])
    else:
        if a[i+1] < a[i] and a[i-1] < a[i]:
            new.append(a[i])
print("Peak value list is: ",new)
sum = 0
for i in new:
    sum = sum+i
print("sum: ",sum)
    