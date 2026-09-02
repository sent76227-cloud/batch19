'''https://leetcode.com/problems/two-sum/submissions/2123011987/'''


n = int(input("Enter n"))
target = int(input("Enter target: "))
l = []
for i in range(n):
    a = int(input("Enter "))
    l.append(a)
print(l)
for i in range(0,len(l)):
    x = 0
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            print(i,j)
            x = 1
            break
    if x == 1:
        break
        
    