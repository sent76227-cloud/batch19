'''19 Find the highest frequency character. '''

s = input("Enter sting: ")
hig = s[0]
max = -1
for i in range(len(s)):
    count = 0
    for j in range(i,len(s)):
        if s[i] == s[j]:
            count = count + 1
            
    if max < count:
        max = count
print("Max",s[max],"=",max)
    
    