'''48Remove all vowels.
example:
    S = "aeiou XYZ" " XYZ"'''
s = input("Enter string: ")
vowel =  "aeiou"
new = ""
for i in s:
    if i not in vowel:
        new = new +i
print(new)