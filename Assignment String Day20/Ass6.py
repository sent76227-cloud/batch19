'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:


iphone is good and iphone battery is strong


Word:


iphone


Output:


2


'''
s=input("Enter string: ")
word=input("Enter word: ")
s=s.lower()
s=s.split()
count=0
for i in range(0,len(s)):
     if word in s[i]:
         count+=1
print(count)