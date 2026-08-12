'''17 Remove occurrences of a character.'''
s = input("Enter Sting: ")
a = input("Enter Occurrences of Character: ")
new = ""
for i in s:
    if i != a:
        new = new + i
print(new)
        