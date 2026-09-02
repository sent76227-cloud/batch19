'''57Merge two strings alternatively (char by char). 
example
    S1 = "ABC", S2 = "def" 
    output = "AdBeCf"
    '''
s1 = input("Enter s1 string: ")
s2 = input("Enter S2 stirng: ")
merge = s1+s2
new = ""
a  = 0
b = 0
for i in range(len(merge)):
        if i%2 == 0 :
            new = new + s1[a]
            a = a+1
        else:
            new = new + s2[b]
            b = b+1
print("Merge ",new)
        
