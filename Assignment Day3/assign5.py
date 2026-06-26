'''
Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
'''
print("Accepts marks of 3 subjects.")
print("Calculates average.")
hindi,english,maths = map(int,input("Enter hindi english maths: ").split( ))
avg = (hindi + english +maths )/3
print(f"Average = {avg}") 
