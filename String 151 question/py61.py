'''61 Count total alphabets, digits, and special characters. 
S = "a1b!c2" 
Alphabets: 3, 
Digits: 2, 
Special: 1
'''
s =  input("Etner a sting: ")
alp = ""
dig = ""
spec= ""
for i in s:
    if i >= "0" and i <= "9":
        dig = dig+i
    elif i>= "a" and i <= "z":
        alp = alp+i
    else:
        spec = spec+i
print("Alphabet's ",len(alp))
print("Digit's",len(dig))
print("Special: ",len(spec))
        