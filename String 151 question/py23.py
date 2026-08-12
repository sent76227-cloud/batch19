'''23 Print all characters that occur exactly twice'''

s = input("Enter sting: ")
count = 0
twice = ""
for i in s:
    count = s.count(i)
    if count == 2:
        twice = twice + i
print(twice)
uni = ""
for i in twice:
    if i not in uni:
        uni =  uni + i
print(uni)