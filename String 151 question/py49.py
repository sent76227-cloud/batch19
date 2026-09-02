'''49Replace all consonants with ''.
example :
    S = "apple" "ae" '''
s = input("Enter sting: ")
vovel = "aeiou"
new = ""
for i in s:
    if i in vovel:
        new = new+i
print(new)