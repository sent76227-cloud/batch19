'''QNO 1: Matrix Transpose & Diagonal Transformation(3.5 marks)

Write a Python program that accepts an N × N square matrix from the user.

The program must:

Display the original matrix.
Find and display the Main Diagonal elements.
Find and display the Secondary Diagonal elements.
Create the transpose of the matrix.
In the transposed matrix, swap each Main Diagonal element with the corresponding Secondary Diagonal element.
Display the final matrix.
The original matrix must not be modified.
Input
Enter the size of matrix: 4

Enter matrix elements:
10 20 30 40
50 60 70 80
90 15 25 35
45 55 65 75
Expected Output
Original Matrix:
10 20 30 40
50 60 70 80
90 15 25 35
45 55 65 75

Main Diagonal Elements:
10 60 25 75

Secondary Diagonal Elements:
40 70 15 45

Transpose Matrix:
10 50 90 45
20 60 15 55
30 70 25 65
40 80 35 75

Final Matrix After Diagonal Swapping:
45 50 90 10
20 15 60 55
30 25 70 65
75 80 35 40


Conditions
Use Python nested lists.
Matrix size must be taken from the user.
Do not use NumPy.
Do not use zip().
Do not use built-in matrix operations.
Do not modify the original matrix. '''


n = int(input("Enter the size of matrix: "))

matrix = []

print("Enter matrix elements:")

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)


# Original Matrix
print("\nOriginal Matrix:")

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


# Main Diagonal
print("\nMain Diagonal Elements:")

main_diagonal = []

for i in range(n):
    main_diagonal.append(matrix[i][i])

print(*main_diagonal)


# Secondary Diagonal
print("\nSecondary Diagonal Elements:")

secondary_diagonal = []

for i in range(n):
    secondary_diagonal.append(matrix[i][n - i - 1])

print(*secondary_diagonal)


# Transpose Matrix
transpose = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix[j][i])
    transpose.append(row)


print("\nTranspose Matrix:")

for i in range(n):
    for j in range(n):
        print(transpose[i][j], end=" ")
    print()


# Swap Main Diagonal and Secondary Diagonal
for i in range(n):
    main_col = i
    secondary_col = n - i - 1

    temp = transpose[i][main_col]
    transpose[i][main_col] = transpose[i][secondary_col]
    transpose[i][secondary_col] = temp


# Final Matrix
print("\nFinal Matrix After Diagonal Swapping:")

for i in range(n):
    for j in range(n):
        print(transpose[i][j], end=" ")
    print()


