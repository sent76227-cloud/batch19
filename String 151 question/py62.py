'''62 Count vowels and consonants. 
S = "apple" 
Vowels: 2, 
Consonants: 3
'''
s = input("Enter a sting: ")
vowel = "aeiou"
vov = ""
const = ""
for i in s:
    if i in vowel:
        vov = vov+i
    else:
        const = const+i
print("Vowels: ",len(vov))
print("Consonants: ",len(const))
        