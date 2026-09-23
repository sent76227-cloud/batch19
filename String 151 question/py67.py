'''
67. Count how many times a substring appears. 
S = "abab", 
Sub = "ab" 
- 2
'''
s = input("Enter stringg: ")
sub=  input("Enter sub-string: ")
for i in s:
    for j in sub:
        if i == j:
            