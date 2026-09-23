'''63 Count frequency of each character. 
S = "aabcc"
a: 2, b: 1, c: 2'''
s = input("Enter sting: ")
uniq = ""
for i in s:
    if i not in uniq:
        uniq = uniq+i

for i in uniq:
    count = 0
    for j in s:
        if i == j:
            count = count+1
    print(i," = ",count)