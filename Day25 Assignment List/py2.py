'''2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''
l = list(map(str,input("Enter list of: ").split()))

for i in range(len(l)):
    for j in range(i+1,len(l)):

        x =  True
        for ch in l[i]:
            if ch in l[j]:
                x = False
                break
        if x == True :
            print(l[i],"And ",l[j])
            



        
           