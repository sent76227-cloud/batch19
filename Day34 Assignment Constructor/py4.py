'''
Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B
'''
class student:
    def __init__(self,roll_no,std_name,marks1,marks2,marks3):
        self.roll_no =roll_no
        self.std_name =std_name
        self.marks1 =marks1
        self.marks2 =marks2
        self.marks3 = marks3
    def calculation(self):
        self.totalmarks = self.marks1+ self.marks2 +self.marks3
        self.per = (self.totalmarks/300)*100
        if self.per >= 90:
            self.grade = "A" 
        elif self.per >= 75:
            self.grade = "B"
        elif self.per >= 60:
            self.grade = "C"
        else:
            self.grade = "D"
    def display(self):
        print("------ Student Result ------")
        print("Roll Number: ",self.roll_no)
        print("Student Name: ",self.std_name)
        print("Total Marks: ",self.totalmarks)
        print("Total percentage: ",self.per)
        print("Grade: ",self.grade)

roll_no = int(input("Enter roll_no: "))
std_name = input("Enter Name: ")
marks1 =  int(input("Enter marks 1 : "))
marks2 =  int(input("Enter marks 2 : "))
marks3 = int(input("Enter marks 3 "))
s1 = student(roll_no,std_name,marks1,marks2,marks3)
s1.calculation()
s1.display()
        
        