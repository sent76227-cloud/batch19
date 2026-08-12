'''
6.

 Frequency Count of Elements (Advanced Scenario-Based Problem)


A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).

The department wants to analyze:

* How many times each option was selected
* Most popular option
* Least popular option
* Detect invalid entries (negative numbers or zeros)

---

 Requirements

Write a Python program to:

1. Store survey responses in a list
2. Ignore invalid entries (≤ 0)
3. Count frequency of each valid number
4. Display frequency in sorted order
5. Find the most frequently selected option
6. Find the least frequently selected option (excluding invalid data)
7. Store frequency in a dictionary

---


NOTE:
* Avoid using built-in `Counter`

## Input Format

A list of integers representing responses.

---

# Scenario 1: Normal Survey Data

## Input

[1, 2, 2, 3, 3, 3, 4, 1, 2]

## Output

```
Frequency Count:
1 → 2
2 → 3
3 → 3
4 → 1

Most Frequent: 2 or 3 (tie)
Least Frequent: 4
```

---

# Scenario 2: Data with Invalid Entries

## Input

[1, 2, -1, 3, 0, 2, 4, -5, 3, 3]

## Output

```
Invalid Entries Ignored: [-1, 0, -5]

Frequency Count:
1 → 1
2 → 2
3 → 3
4 → 1

Most Frequent: 3
Least Frequent: 1 or 4
```

---

# Scenario 3: Highly Skewed Data

## Input

[5, 5, 5, 5, 2, 2, 1]

## Output

```
Frequency Count:
1 → 1
2 → 2
5 → 4

Most Frequent: 5
Least Frequent: 1
```

---

# Scenario 4: All Same Values

## Input

[7, 7, 7, 7, 7]

## Output

```
Frequency Count:
7 → 5

Most Frequent: 7
Least Frequent: 7
```

---

# Scenario 5: Empty / Invalid Only Data

## Input

[-1, 0, -3]

## Output

```
No valid data found
```

--'''
a = list(map(int,input("Enter list number: ").split()))
uniq = []
new = []
for i in a:
    if i not in uniq:
        uniq.append(i)
#print("Unique: ",uniq)
for i in range(0,len(uniq)):
    freq = 0
    for j in range(0,len(a)):
        if uniq[i] == a[j]:
            freq = freq + 1        
    new.append(freq)
uniq.sort()
new.sort()
print("Unique",uniq)
print("frequency",new)



for n,m in zip(uniq,new):
    if 0 < n and 0 < m:   
        print(n,"->",m)

lar = new[0]
small = new[0]
for i in new:
    if lar < i:
        lar = i
    if i < small:
        small = i
print("Highest Frequency number: ",end="")
hig = []
for i in range(len(new)):
    if new[i]==lar and 0 < uniq[i]:
        hig.append(uniq[i])
a = len(hig)
for i in range(len(hig)):
    print(hig[i],end=" ")
    if i < a-1  :
        print("or",end=" ")
        
print()
print("Lowest Frequency number: ",end="")
low = []
for i in range(len(new)):
    if new[i] == small and 0 < uniq[i] :
        
        
        low.append(uniq[i])
b = len(low)
for i in range(len(low)):
    print(low[i],end ="")
    if i < b-1:
        print(" or",end=" ")
    
    
        
    
        
    


