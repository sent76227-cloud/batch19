'''https://leetcode.com/problems/remove-duplicates-from-sorted-array/'''
n = int(input("Enter n"))

l = []
for i in range(n):
    a = int(input("Enter "))
    l.append(a)


uniq = []
for i in l:
    if i not in uniq:
        uniq.append(i)
        
l = uniq
print(uniq)
print(l)
        

