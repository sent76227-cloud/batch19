'''56Reverse only consonants. 
example 
    S = "apple" "eplpa" {wrong example}
    S = "apple" "alppe" {right example}

    
'''
s= input("Enter string: ")
vovel = "aeiou"
conc = ""
value = ""
for i in s:
    if i not in vovel:
        conc =  i+conc
        
    else:
        value = value + i
        
print(value)
print(conc)
new = ""
j = 0
for i in range(len(s)):
    if s[i] not in vovel:
        new = new + conc[j]
        j = j+1
        
    else:
        new = new + s[i]
        
print(new)

            