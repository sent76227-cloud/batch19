'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop ''' 



s = input("Enter sting: ")
word = s.split()
length = len(word)

for i in range(0,length):
   rev = ""
   w = word[i]
   rev = w[::-1]
   print(rev,end=" ")