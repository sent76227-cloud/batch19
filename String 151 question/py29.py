'''29 Remove occurrences of a word. '''
s = input("Enter sting: ")
word = input("Enter word: ")

a = s.split()
new = ""
for i in a:
    if i not in new and i !=word:
        new = new+i
print(new)