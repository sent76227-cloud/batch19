'''5 Compare two strings ignoring case.'''
a = False
s1 = input("enter string: ").lower()
s2 = input("enter string: ").lower()

if s1 == s2:
    a = True

if a == True:
    print("Same s1 and s2")
else:
    print("Not equal (or non - zero value)")