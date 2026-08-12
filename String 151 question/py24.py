'''24 Check if all characters in a string are unique. '''

s =  input("Enter sting: ")
uni = ""
for i in s:
    if i not in uni:
        uni = uni+i
if uni == s:
    print(True)
else:
    print(False)
    