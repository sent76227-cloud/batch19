'''64 Count frequency of each vowel. 
S = "programming" 
o: 1, a: 1 (e, i, u: 0)
'''
s =  input("Enter sting: ")
vovel = "aeiou"
for i in vovel:
    count = 0
    for j in s:
        if i == j:
            count = count+1
        
    print(i,"= ",count)
    