'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''

first = input("Enter First Product Code: ").lower()
second = input("Enter Second Product Code: ").lower()
firstlen = len(first)
secondlen = len(second)
i = 0
match = True 
while i < firstlen:
    ch = first[i]
    if ch == " ":
         i = i+1
         continue
   
    j = 0
    found = False
    while j < secondlen:
             sch = second[j]
             if sch == " ":
                 j = j+1
                 continue
             elif ch == sch:
                  second = second[:j] + "*" +  second[j+1:]
                  found = True
                  break
             j = j+1
    if found == False:
          match = False
          break
    i = i+1  
j = 0
while j < secondlen:
      if second[j] != " " and second[j] != "*":
              match =  False
              break
      j = j+1
if match:
    print("Both Product codes are matching")
else:    
    print("Both product codes are not matching")





             