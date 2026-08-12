'''4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

---
'''
s = list(map(int,input("Enter list: ").split()))
s.sort()
print(s)
x = 0
new = []
for i in range(len(s)):
    a = s[i]
    for j in range(i+1,len(s)):
        if a+1 == s[j] :
            new.append(a)
        
        
sum = new[len(new)-1]+1    
new.append(sum)
print(new)
print("Longest Consecutive Length = ",len(new))
