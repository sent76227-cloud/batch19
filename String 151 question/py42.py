'''42 Check if two strings are equal without equals(). '''

s1 = input("Enter Sting : ")
s2 = input("Enter sting 2: ")
equal = True
for i in range(len(s1)):
    for j in range(len(s2)):
        if i+j<len(s1) and s1[i+j]==s2[j] :
            equal = True
        else:
            equal = False
    if equal ==  True:
        break
if equal == True and len(s1) == len(s2):
    print("string is equal")
else:
    print("sting is not equal")
            
