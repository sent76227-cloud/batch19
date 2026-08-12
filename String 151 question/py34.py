'''34 Find the shortest word. '''

s = input("Enter sting: ")
a = s.split()
short = len(a[0])

for i in a:
    if short > len(i):
        short = len(i)
print(short,"- ",end = " ")
for i in a:
    if short == len(i):
        print(i)