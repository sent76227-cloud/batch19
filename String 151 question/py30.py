'''30 Replace a word with another word.'''
s = input("Enter sting: ")
word = input("Enter word: ")
newword = input("Enter new word: ")

a = s.split()
new = ""
for i in a:
    if i == word:
        new = new + newword
    else:
        new = new + i
print(new)
        