'''8 Toggle the case of each character.'''

s = input("enter string: ")
togal = ""
for i in s:
    if i.isupper():
        togal = togal+i.lower()
    else:
        togal = togal+i.upper()
print(togal)