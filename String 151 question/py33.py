'''33 Find the longest word'''

s = input("Enter sting: ")
a = s.split()
log = len(a[0])

for i in a:
    if log < len(i):
        log = len(i)
print(log,"- ",end = " ")
for i in a:
    if log == len(i):
        print(i)