'''4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''

a = list(map(int,input("enter list: ").split()))
palan = []
for i in a:
    check = i
    rev = 0
    j = check
    while 0 < j:
        dig = check%10
        rev = rev*10+dig
        check = check//10
        j = j//10
    if i == rev:
        palan.append(rev)
print("Palandromes: ",palan)
print("Count: ",len(palan))
lar = palan[0]
for i in palan:
    if lar < i:
        lar = i
print("Lagrest Palandrome is",lar)
shorted = sorted(palan)
print("sorted of Palandrome is ",shorted)
        
