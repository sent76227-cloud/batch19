'''=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92





{ek bar man se krke dekhna hai }
'''



from collections import namedtuple

student = namedtuple("Student", ["roll_no", "name", "course", "marks"])

n = int(input("Enter number of students: "))

students = []

# 1. Read student records
for i in range(n):
    roll_no, name, course, marks = input().split()

    s = student(int(roll_no), name, course, int(marks))
    students.append(s)


# 2. Display all student details
print("\nAll Students:")
for s in students:
    print(s.roll_no, s.name, s.course, s.marks)


# 3. Find topper
topper = students[0]

for s in students:
    if s.marks > topper.marks:
        topper = s

print("\nTopper:")
print(topper.roll_no, topper.name, topper.course, topper.marks)


# 4. Count students scoring above 80
count = 0

for s in students:
    if s.marks > 80:
        count += 1

print("\nStudents Above 80:")
print(count)


# 5. Calculate average marks
total = 0

for s in students:
    total += s.marks

average = total / n

print("\nAverage Marks:")
print(average)


# 6. Search students by course
search_course = input("\nEnter course: ")

print("\nStudents in", search_course, "Course:")

for s in students:
    if s.course == search_course:
        print(s.roll_no, s.name, s.course, s.marks)












































































"""
{mene try kiya hai yehh}

from collections import namedtuple
student = namedtuple("field",["roll_no","name","course","marks"])
n = int(input("Enter number ofstudents: "))
emp = []
for i in range(n):
    emp_roll = int(input("Enter Roll number: "))
    emp_name = input("Enter name: ")
    depart = input("Enter Course: ")
    salary_of_emp = int(input("Enter marks: "))
    s = student(emp_roll,emp_name,depart,salary_of_emp)
    emp.append(s)
for i in emp:
    print(i.roll_no,i.name,i.course,i.marks)

max = emp[0].marks
for i in emp:
    course = input("Enter course: ")
    if course == i.course:
        if max<i.marks:
            max = i.marks

for i in emp:
    if course == i.course and max == i.marks:
        print(i.roll_no,i.name,i.course,i.marks)
      """  
    