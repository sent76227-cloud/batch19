'''.
MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit
Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4'''

# MATRIX PATTERN DETECTION SYSTEM

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []

# Input matrix
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


while True:

    print("\nMenu")
    print("1. Count Even Numbers Above Main Diagonal")
    print("2. Count Odd Numbers Below Main Diagonal")
    print("3. Display Boundary Elements")
    print("4. Exit")

    choice = int(input("Enter choice: "))


    # Choice 1
    if choice == 1:

        count = 0
        even_numbers = []

        for i in range(n):
            for j in range(m):

                if j > i and matrix[i][j] % 2 == 0:
                    count += 1
                    even_numbers.append(matrix[i][j])

        print("Even Numbers Above Main Diagonal =", count)
        print(tuple(even_numbers))


    # Choice 2
    elif choice == 2:

        count = 0
        odd_numbers = []

        for i in range(n):
            for j in range(m):

                if i > j and matrix[i][j] % 2 != 0:
                    count += 1
                    odd_numbers.append(matrix[i][j])

        print("Odd Numbers Below Main Diagonal =", count)
        print(tuple(odd_numbers))


    # Choice 3
    elif choice == 3:

        boundary = []

        for i in range(n):
            for j in range(m):

                # First row
                if i == 0:
                    boundary.append(matrix[i][j])

                # Last row
                elif i == n - 1:
                    boundary.append(matrix[i][j])

                # First column
                elif j == 0:
                    boundary.append(matrix[i][j])

                # Last column
                elif j == m - 1:
                    boundary.append(matrix[i][j])

        print("Boundary Elements:")

        for x in boundary:
            print(x, end=" ")

        print()


    # Choice 4
    elif choice == 4:
        print("Program ended.")
        break


    else:
        print("Invalid choice")