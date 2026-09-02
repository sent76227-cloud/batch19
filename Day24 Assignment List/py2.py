'''2.
=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

=========================================================
'''
r1 = int(input("Enter Row1: "))
c1 = int(input("Enter colom 1 : "))
matrix1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input("Element's :")))
    matrix1.append(row)    
print(matrix1)
while True:
    print("1. Prime number Row wise: ")
    print("2.Perfect number colom wise: ")
    print("3.Display Row wise sum: ")
    print("4.exit")
    choice = int(input("Emter your choice: "))
    match choice:
        case 1:
            colom = []
            
            for i in range(len(matrix1)):
                row =  []
                
                count = 0
                count1 = 0
                for j in range(len(matrix1[i])):
                    value = matrix1[i][j]
                    flag = 0
                    
                    for x in range(2,value):
                        if value%x == 0:
                            flag = 1
                            break
                    if flag == 0:
                        row.append(matrix1[i][j])
                        count = count+1
                    else:
                        row.append(0)
                count1 = count1+1
                print("Prime number is row:",count1," - ",count)
            
            
        case 3 :
            colom = []
            count = 0
            for i in range(len(matrix1)):
                sum = 0
                for j in range(len(matrix1[i])):
                    sum = sum+matrix1[i][j]
                count = count+1
                print("Sum of Element Row:",count,"-",sum)
        case 2:
            colom = []
            count = [0]*len(matrix1[0])
            for i in range(len(matrix1)):
                row = []
                for j in range(len(matrix1[i])):
                    value = matrix1[i][j]
                    fac = 0
                    
                    for x in range(1,value):
                        if value%x==0:
                            fac = fac+x
                    if fac == value:
                        count[j] = count[j]+1
                        row.append(matrix1[i][j])
                    else:
                        row.append(0)
                colom.append(row)
                
            print(colom)
            print(count)
        case 4:
            break

                    
                            
                    