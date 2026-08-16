'''43 Check if two strings are rotations of each other'''

s1 = input("Ener sting1: ")
s2 =  input("Enter sting2: ")

sort = ""
mix = s1[0]
for i in s1:
    if  i < mix :
        mix = i
        sort = sort+i
    else:
        sort = i+sort
print(sort)