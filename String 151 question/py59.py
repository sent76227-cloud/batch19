'''59 Rotate characters by 3 positions to the right. 
example:  
    S = "abcde"
output: 
    "cdeab"
    '''
s =  input("Enter sting: ")
n = int(input("Enter possition you want to rotate :"))
new = ""
last = ""
reg = ""
for i in range(len(s)):
    if n-1 > i:
        last = last + s[i]
    else:
        reg = reg +s[i]
print(last)
print(reg)
merge = reg + last
print(merge)
