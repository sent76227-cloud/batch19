'''Assignment 1: Student Result Calculator'''

class Student:
    def attribute(self, name, roll_number, english, mathematics, science):
        self.name = name
        self.roll_number = roll_number
        self.english = english
        self.mathematics = mathematics
        self.science = science

    def calculate_total(self):
        self.total = self.english + self.mathematics + self.science

    def calculate_percentage(self):
        self.percentage = (self.total / 300) * 100

    def display_result(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Total Marks:", self.total)
        print("Percentage:", self.percentage, "%")


student = Student()
student.attribute(input("Enter name: "), int(input("Enter roll number: ")),
                  int(input("Enter English marks: ")),
                  int(input("Enter Mathematics marks: ")),
                  int(input("Enter Science marks: ")))
student.calculate_total()
student.calculate_percentage()
student.display_result()
