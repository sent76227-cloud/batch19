'''22 Find the last repeating character. '''
s = input("Enter sting: ")

count = 0
result = ""
for i in s:
    count = s.count(i)
    if count > 1:
        result = result+i
uni = ""
for i in result:
    if i not in uni:
        uni = uni+i
    

print(uni[len(uni)-1])