'''
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed'''
isbn = set()

while True:

    print("\nMenu")
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        number = input("Enter ISBN: ")

        # Set does not store duplicate ISBN
        isbn.add(number)

    elif choice == 2:

        number = input("Enter ISBN: ")

        if number in isbn:
            isbn.remove(number)
            print("ISBN Removed")
        else:
            print("ISBN Not Found")

    elif choice == 3:

        number = input("Enter ISBN: ")

        if number in isbn:
            print("ISBN Found")
        else:
            print("ISBN Not Found")

    elif choice == 4:

        print("ISBN Numbers:")
        print(isbn)

    elif choice == 5:

        print("Total Books:")
        print(len(isbn))

    elif choice == 6:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")