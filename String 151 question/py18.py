'''18 Replace occurrences of a character. '''
s = input("Enter sting: ")
old = input("Enter which chr you want to replace: ")
new = input("Enter That you wnat to put: ")
str = ""
for i in s:
    if i == old:
        str = str + new
    else:
        str = str + i
print(str)