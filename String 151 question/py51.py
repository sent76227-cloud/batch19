''' 51Extract only digits.
exampel:
    S = "a1b2c3" "123"  
    '''
s = input("Enter sting: ")
new = ""
for i in s:
    if i>="0" and i<="9":
        new = new +i
print(new)