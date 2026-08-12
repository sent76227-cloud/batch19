'''26 Find the first occurrence of a word. '''
s = input("Enter string: ")
word = input("Enter word: ")
a = s.split()
index = 0
for i in range(len(a)):
    index = index + len(a[i])
    print(a[i])
    if a[i] == word:
        print("Matced")
        print(index - len(a[i])+len(a)-1)
        break

        