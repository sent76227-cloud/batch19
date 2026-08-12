'''28 Count occurrences of a word. '''
s = input("Ente sting: ")
occ = input("Enter word: ")
a = s.split()
count = 0
for i in a:
    if i == occ:
        count = count+1
print("Count ",count)
