'''40 Search all occurrences of a word. '''
s = input("Enter sting: ")


ch = input("Enter character: ")
for i in range(len(s)):
    if ch == s[i]:
        print(i,end=" ")