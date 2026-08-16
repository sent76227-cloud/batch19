'''7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z.'''
sentence = ""

# Set containing all alphabets
alphabets = set("abcdefghijklmnopqrstuvwxyz")

while True:

    print("\nMenu")
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        sentence = input("Enter Sentence: ")

    elif choice == 2:

        # Convert sentence to lowercase
        sentence = sentence.lower()

        # Convert sentence characters into a set
        present = set(sentence)

        # Find alphabets which are not present
        missing = alphabets.difference(present)

        print("Missing Alphabets:")
        print(missing)

    elif choice == 3:

        sentence = sentence.lower()

        present = set(sentence)

        missing = alphabets.difference(present)

        print("Count of Missing Alphabets:")
        print(len(missing))

    elif choice == 4:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")