'''44Check if two strings are anagrams'''
#example - S1 = "listen", S2 = "silent"
s1 = input("Enter sting 1 : ")
s2 = input("Enter sting 2: ")
new = ""
count = 0
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if s1[i] == s2[j]:
            new = new+s1[i]
            break
if new == s1 :
    print("Anagram")
else:
    print("Not Anagram ")
             
            