'''13 Get the Unicode code point before index'''
s = input("Enter a sting: ")
a = input("Enter a character: ")


for i in range(len(s)):
    if s[i] == a:
        print(ord(s[i-1]),"( Unicode for",s[i-1],")")
        break
    