'''35 Find the first palindrome word. '''

s = input("Enter sting: ")
a = s.split()

for i in range(len(a)):
    word = a[i]
    
    rev = ""
    j =  len(word)-1
    while 0<=j:
        rev = rev+word[j]
        j = j-1
    if rev == word:
        print(word)
        break
