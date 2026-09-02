'''53Remove all punctuation characters. 
example: 
    S = "Hello, world!" 
    "Hello world" 
    '''
s = input("Enter sting: ")
new = ""
pancutation ="!"
for i in s:
    if i not in pancutation:
        new = new +i
print(new)