'''60Append two strings but remove duplicate adjacent characters. 
example: 

    S1 = "miss", 
    S2 = "issippi" 
output: "misisipi"

'''
s1 = input("Enter s1: ")
s2 =  input("Enter s2: ")
uni1 = ""
for i in s1:
    if i not in uni1:
        uni1 = uni1 + i
uni2 = ""
for i in s2:
    if i not in uni2:
        uni2 = uni2 + i
merge = uni1+uni2
print(uni1)
print(uni2)
print(merge)