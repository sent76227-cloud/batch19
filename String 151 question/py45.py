'''45Check whether a string starts/ends with another string.'''
#S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True
s = input("Enter sting: ")
pre = input("Enter prefix: ")
suf = input("Enter Suffix: ")
a = s.split()
if a[0] == pre :
    print(True)
else:
    print("False")
if a[-1] == suf:
    print(True)
else:
    print(False)