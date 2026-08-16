'''41 Check if a string contains a substring (without using built-in method)'''


s = input("Enter string: ")
sub = input("Enter any substring: ")

new = ""

for i in range(len(s)):
    j = 0

    while j < len(sub):
        if i + j < len(s) and s[i + j] == sub[j]:
            new = new + sub[j]
            j = j + 1
        else:
            break

    if len(new) == len(sub):
        break

print(new)
            
        
        
