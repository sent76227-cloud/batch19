'''52Remove all special characters. 
example :
    S = "a!@b#c"
    "abc"'''
s = input("Enter sting: ").lower()
new = ""
for i in s:
    if i>="a" and i<="z":
        new = new+i
    elif i>="0" and i<="9":
        new = new+1
print(new)
    