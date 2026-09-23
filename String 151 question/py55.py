'''55Reverse only vowels. 
example: 
    S = "hello" "holle" 
    '''
#Optimize code
s= input("Enter string: ")
vovel = "aeiou"
value = ""
conc = ""
for i in s:
    if i in vovel:
        value = i+value
    else:
        conc =  conc + i
        

new = ""
j = 0
while j < len(value):
    for i in range(len(s)):
        if s[i] in vovel:
            new = new + value[j]
            j = j+1
        else:
            new = new + s[i]
print(new)
            
    


















'''s = input("Enter sting: ")
vovel = "aeiou"
new = ""
pre = ""
ind = ""
sec = ""
ind2 = ""
for i in range(len(s)):
    x = 0
    if s[i] in vovel:
        pre = s[i]
        ind = i
        for j in range(i+1,len(s)):
            if s[j] in vovel:
                sec = s[j]
                ind2 = j
                x = 1
                break
        if x == 1:
            break
            

new = ""
for i in range(len(s)):
    if i == ind:
        new = new+sec
    elif i == ind2:
        new = new+pre
    else:
        new = new+s[i]
print(new)
        '''    

