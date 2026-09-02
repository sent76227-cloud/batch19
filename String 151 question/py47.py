'''47Check for substring using concatenation trick. 
example : 
        S1="CDAB", S2="ABCD True (S1 is in S2+S2)
"'''
s1 = input("Enter s1: ")
s2 = input("Enter s2: ")
found = s2+s2


if s1 in found:
    print(True)
else:
    print(False)
