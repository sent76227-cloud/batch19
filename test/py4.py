s= input("Enter the sting: ")
s1= input("Enter the sting 1: ")
word = s.split()

count = 0
for n in range(0,len(word)):
    ch = word[n]
    if s1 in word: 
      count = count+1
print(count)
