'''10 Trim leading, trailing, or extra spaces'''

s = input("enter sting: ")
word = s.split()
for i in word:
    print(i,end=" ")