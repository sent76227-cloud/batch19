'''20 Find the lowest frequency character. '''
s = input("Enter sting: ")
min_freq = len(s)
min_char = ""

for ch in s:
    count = s.count(ch)

    if count < min_freq:
        min_freq = count
        min_char = ch
    

result = ""
for i in s:
    if s.count(ch) == min_freq and i not in result:
        result = result+i
print()
for i in result:
    print(i,end=" ")
    
print("Lowest frequency character:", min_char)
print("Frequency:", min_freq)
    