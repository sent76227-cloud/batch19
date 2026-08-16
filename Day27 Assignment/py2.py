'''=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.'''
python_students = set()
java_students = set()

while True:

    print("\nMenu")
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        email = input("Enter Student Email: ")
        python_students.add(email)

    elif choice == 2:
        email = input("Enter Student Email: ")
        java_students.add(email)

    elif choice == 3:
        print("Python Students:")
        print(python_students)

    elif choice == 4:
        print("Java Students:")
        print(java_students)

    elif choice == 5:
        both = python_students.intersection(java_students)
        print("Students in Both Courses:")
        print(both)

    elif choice == 6:
        only_python = python_students.difference(java_students)
        print("Students Only in Python:")
        print(only_python)

    elif choice == 7:
        only_java = java_students.difference(python_students)
        print("Students Only in Java:")
        print(only_java)

    elif choice == 8:
        email = input("Enter Student Email: ")

        if email in python_students:
            print("Student is enrolled in Python")
        else:
            print("Student is not enrolled in Python")

    elif choice == 9:
        all_students = python_students.union(java_students)
        print("Total Unique Students:")
        print(len(all_students))

    elif choice == 10:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")