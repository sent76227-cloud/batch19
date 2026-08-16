'''8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.'''
allowed = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
)

# Empty username initially
username = ""

while True:

    print("\nMenu")
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        username = input("Enter Username: ")

    elif choice == 2:

        valid = True

        # Check every character of username
        for ch in username:

            if ch not in allowed:
                valid = False
                break

        if valid:
            print("Valid Username")
        else:
            print("Invalid Username")

    elif choice == 3:

        print("Allowed Characters:")
        print(allowed)

    elif choice == 4:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")