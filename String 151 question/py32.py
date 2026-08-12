'''32 Count frequency of each word.'''
s = input("Enter words: ")
a = s.split()
uniq = ""

for i in a:
    if i not in uniq:
        uniq = uniq+i+" "
unisplit = uniq.split()
print(s)
for i in unisplit:
    count = 0
    for j in a:
        if i == j:
            count = count+1
    print(i,"=" ,count )
            