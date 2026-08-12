'''21 Find the first non-repeating character. '''

s = input("Enter sting: ")

count = 0
for i in s:
    count = s.count(i)
    if count == 1:
        print(i)
        break
    