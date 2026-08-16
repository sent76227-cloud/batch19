# =========================================
# QUESTION 3: WEBSITE VISITOR TRACKING SYSTEM
# =========================================

# Set to store unique visitor IDs
visitors = set()

while True:

    print("\nMenu")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        visitor = input("Enter Visitor ID: ")

        # add() automatically ignores duplicate values
        visitors.add(visitor)

    elif choice == 2:

        visitor = input("Enter Visitor ID: ")

        # Check before remove to avoid error
        if visitor in visitors:
            visitors.remove(visitor)
            print("Visitor Removed")
        else:
            print("Visitor Not Found")

    elif choice == 3:

        visitor = input("Enter Visitor ID: ")

        if visitor in visitors:
            print("Visitor Found")
        else:
            print("Visitor Not Found")

    elif choice == 4:

        print("All Visitors:")
        print(visitors)

    elif choice == 5:

        print("Unique Visitors:")
        print(len(visitors))

    elif choice == 6:

        visitors.clear()
        print("Visitor Data Cleared")

    elif choice == 7:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")