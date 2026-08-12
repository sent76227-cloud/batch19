'''16 Count total occurrences of a character. '''

s = input("Enter Sting: ")
a = input("Enter Character: ")
count = 0
for i in range(len(s)):
    if s[i] == a:
        count = count + 1
print(count)