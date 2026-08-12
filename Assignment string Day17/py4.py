'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
 '''


name = input("Enter student name: ").lower()


cons = 0
space = 0
vovel = 0
length = len(name)

i = 0
while i < length:
      ch = name[i]
      if ch == "a" or ch =="e" or  ch =="i" or ch =="o" or ch =="u":
            vovel = vovel+1
      elif ch == " ":
            space = space+1 
      else:
            cons =  cons+1
         
          
      i = i+1
print(f"Total consonants : {cons} ")
print()
print(space)