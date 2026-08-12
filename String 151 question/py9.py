'''9 Check whether a string is empty.'''

s = input("enter sting: ")
x = 0
for i in s:
    if i.isspace():
        x = 1
if x == 0:
    print("Not any Space ")
else:
    print("Space in sting")