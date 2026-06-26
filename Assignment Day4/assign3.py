'''
Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
'''
hindi, english, maths, science,sanskrit = map(int,input("Enter Marks: ").split(","))
total = hindi + english + maths + science + sanskrit
average = total/5
perc = total/500*100
print(f"Total = {total}\nAverage = {average}\nPercentage = {perc}")
