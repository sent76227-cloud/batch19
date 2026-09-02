'''54Replace all duplicate characters with '$'.
example: 
S = "hello" 
"he$lo"'''
s = input("Enter string: ")
uniq = ""
for i in s:
    if i not in uniq:
        uniq = uniq + i
print(uniq)
for i in range(0,len(s)):
    for j in range(0,len(uniq)):
        pre = 
        
        if s[i+j]==s[j]:
'''Not complite'''
            