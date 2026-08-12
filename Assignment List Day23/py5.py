'''5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

---
'''
l =  list(map(int,input("Enter list: ").split()))
sumleft = 0
sumright = 0
midsum  = 0
midd = []
for i in range(len(l)):
    
    if i<len(l)//2:
        sumleft =sumleft+l[i]
    elif i >= (len(l)//2)+1:
        sumright = sumright + l[i]
        
    else:
        midsum = midsum + l[i]
        

if sumleft == sumright:
    print("Midd value is :",midsum)
else:
    print("Not mid value")    
        
        
    
    