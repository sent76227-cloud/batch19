'''38 Reverse words without split(). '''
s = input("Enter sting: ")
rev = ""
for i in s:
    rev = i+" "+rev
print(rev)
    
        