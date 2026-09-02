'''50Remove all digits. 
example 
    S = "a1b2c3" 
    "abc"  '''
s = input("Enter sting: ").lower()
new = ""
for i in s:
    if i >= "a" and i<="z":
        new = new+i
print(new)