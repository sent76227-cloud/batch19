'''3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.

4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.

'''
subjects = frozenset(["Python", "Java", "MySQL", "React", "Spring Boot"])

while True:

    print("\nMenu")
    print("1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        print("Subjects:")
        print(subjects)

    elif choice == 2:

        subject = input("Enter Subject Name: ")

        if subject in subjects:
            print("Subject Found")
        else:
            print("Subject Not Found")

    elif choice == 3:

        print("Total Subjects:")
        print(len(subjects))

    elif choice == 4:

        subject = input("Enter Subject to Add: ")

        # Frozenset cannot be modified using add()
        try:
            subjects.add(subject)
        except AttributeError:
            print("Cannot Add Subject - Frozenset is Immutable")

    elif choice == 5:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")