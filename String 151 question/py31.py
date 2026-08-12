'''31 Remove duplicate words.'''
s = input("Enter Sting: ")
a = s.split()
new = ""
for i in a:
    if i not in new:
        new = new+i+" "
print("Duplicate Words remove: ",new)