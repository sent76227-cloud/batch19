'''36 Reverse order of words. '''

s = input("Enter sting: ")
a = s.split()
rev  = " "
for i in a:
    rev = i+" "+rev
print(rev)