'''58Rotate characters by 2 positions to the left. 
example : 
    S = "abcde" 
output 
    "cdeab"
    '''
s =  input("Enter sting: ")
n = int(input("Enter possition you want to rotate :"))
new = ""
last = ""
reg = ""
for i in range(len(s)):
    if n >i:
        last = last + s[i]
    else:
        reg = reg +s[i]
merge = reg + last
print(merge)