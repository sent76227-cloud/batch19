'''1.
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

******** STUDENT RESULT MANAGEMENT ********

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.

'''
def studentdetails():
    name = input("Enter student name: ")
    rollno = int(input("Enter roll number: "))

    mark1 = int(input("Enter mark 1: "))
    mark2 = int(input("Enter mark 2: "))
    mark3 = int(input("Enter mark 3: "))
    mark4 = int(input("Enter mark 4: "))
    mark5 = int(input("Enter mark 5: "))

    if mark1 < 0 or mark1 > 100:
        print("Invalid marks. Marks should be between 0 and 100.")
        return None

    if mark2 < 0 or mark2 > 100:
        print("Invalid marks. Marks should be between 0 and 100.")
        return None

    if mark3 < 0 or mark3 > 100:
        print("Invalid marks. Marks should be between 0 and 100.")
        return None

    if mark4 < 0 or mark4 > 100:
        print("Invalid marks. Marks should be between 0 and 100.")
        return None

    if mark5 < 0 or mark5 > 100:
        print("Invalid marks. Marks should be between 0 and 100.")
        return None

    return name, rollno, mark1, mark2, mark3, mark4, mark5


def total(mark1, mark2, mark3, mark4, mark5):
    total_marks = mark1 + mark2 + mark3 + mark4 + mark5
    return total_marks


def percentage(mark1, mark2, mark3, mark4, mark5):
    total_marks = total(mark1, mark2, mark3, mark4, mark5)
    per = (total_marks / 500) * 100
    return per


def grade(mark1, mark2, mark3, mark4, mark5):
    per = percentage(mark1, mark2, mark3, mark4, mark5)

    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "Fail"


def highest(mark1, mark2, mark3, mark4, mark5):
    return max(mark1, mark2, mark3, mark4, mark5)


def lowest(mark1, mark2, mark3, mark4, mark5):
    return min(mark1, mark2, mark3, mark4, mark5)


student = None

while True:
    print("******** STUDENT RESULT MANAGEMENT ********")
    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Find Grade")
    print("5. Display Result")
    print("6. Find Highest Mark")
    print("7. Find Lowest Mark")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            student = studentdetails()

            if student is not None:
                print("Student details added successfully.")

        case 2:
            if student is None:
                print("Please add student details first.")
            else:
                name, rollno, mark1, mark2, mark3, mark4, mark5 = student
                print("Total Marks =", total(mark1, mark2, mark3, mark4, mark5))

        case 3:
            if student is None:
                print("Please add student details first.")
            else:
                name, rollno, mark1, mark2, mark3, mark4, mark5 = student
                print("Percentage =", percentage(mark1, mark2, mark3, mark4, mark5))

        case 4:
            if student is None:
                print("Please add student details first.")
            else:
                name, rollno, mark1, mark2, mark3, mark4, mark5 = student
                print("Grade =", grade(mark1, mark2, mark3, mark4, mark5))

        case 5:
            if student is None:
                print("Please add student details first.")
            else:
                name, rollno, mark1, mark2, mark3, mark4, mark5 = student

                print("----------- RESULT CARD -----------")
                print("Name        :", name)
                print("Roll Number :", rollno)
                print("Marks")
                print("Subject 1 :", mark1)
                print("Subject 2 :", mark2)
                print("Subject 3 :", mark3)
                print("Subject 4 :", mark4)
                print("Subject 5 :", mark5)
                print("Total Marks :", total(mark1, mark2, mark3, mark4, mark5))
                print("Percentage  :", percentage(mark1, mark2, mark3, mark4, mark5))
                print("Grade       :", grade(mark1, mark2, mark3, mark4, mark5))
                print("Highest Mark:", highest(mark1, mark2, mark3, mark4, mark5))
                print("Lowest Mark :", lowest(mark1, mark2, mark3, mark4, mark5))

        case 6:
            if student is None:
                print("Please add student details first.")
            else:
                name, rollno, mark1, mark2, mark3, mark4, mark5 = student
                print("Highest Mark =", highest(mark1, mark2, mark3, mark4, mark5))

        case 7:
            if student is None:
                print("Please add student details first.")
            else:
                name, rollno, mark1, mark2, mark3, mark4, mark5 = student
                print("Lowest Mark =", lowest(mark1, mark2, mark3, mark4, mark5))

        case 8:
            print("Thank You. Program Terminated.")
            break

        case _:
            print("You entered a wrong choice.")




    