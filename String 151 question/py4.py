'''4 Compare two strings (case-sensitive).'''
a = False
s1 = input("enter string: ")
s2 = input("enter string: ")

if s1 == s2:
    a = True

if a == True:
    print("Same s1 and s2")
else:
    print("Not equal (or non - zero value)")