'''14 Find the first occurrence of a character. '''
s = input("Enter Sting: ")
a = input("Enter Character: ")
for i in range(len(s)):
    if s[i] == a:
        print("Index ",i)
        break