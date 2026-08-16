'''
1. Remove All Special Characters from a String

Online Banking Customer Data Cleaning System

A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.

Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

* Alphabets
* Numbers
* Spaces

The cleaned value should be stored back into the original string variable.

Input:

Deepika@@ Padukone!! 123
Output:
Deepika Padukone 123
Input:
Ajay###Singh$$$
Output:
AjaySingh
'''

s=input("Enter String: ")
newStr=''
for i in range(0,len(s)):
     if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z') or (s[i]>='0' and s[i]<='9') or s[i]==' ':
          newStr+=s[i]
print(newStr)