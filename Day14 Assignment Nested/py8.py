''' 8.
Online Exam Result Processing System

An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.

Input:
Enter number of classes: 2
Enter students per class: 2
Enter subjects per student: 3

Class 1

Student 1
Enter mark: 70
Enter mark: 80
Enter mark: 90

Student 2
Enter mark: 60
Enter mark: 75
Enter mark: 85

Class 2

Student 1
Enter mark: 88
Enter mark: 77
Enter mark: 66

Student 2
Enter mark: 90
Enter mark: 92
Enter mark: 95

Output:
Class 1
Student 1 Total = 240
Student 2 Total = 220

Class 2
Student 1 Total = 231
Student 2 Total = 277 '''


a = int(input("Enter class  :"))
for n in range(1,a+1):
    student = int(input(f"Enter number of students in class{n} "))
    for i in range(1,student+1):
       subject = int(input("Enter no of subject of student  "))
       total = 0
       for a in range(1,subject+1):
           mark = int(input(f"enter marks of subject {a} "))
           total = mark  +total
       print(total)










