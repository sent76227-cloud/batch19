'''15 Find the last occurrence of a character'''
s = input("Enter Sting: ")
a = input("Enter Character: ")
count = 0
for i in range(len(s)-1,0,-1):
    if s[i] == a:
        print(i)
        break
