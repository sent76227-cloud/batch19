'''4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

========================================================='''
r1 = int(input("Enter Row1: "))
c1 = int(input("Enter colom 1 : "))
matrix1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input("Element's :")))
    matrix1.append(row)    
print(matrix1)
sum2 = 0
sum = 0
while True:
    print("1. Display Main Diagonal Elements: ")
    print("2.Display Secondary Diagonal Elements: ")
    print("3.Compare Main and Secondary Diagonal Sums ")
    print("4.exit")
    choice = int(input("Emter your choice: "))
    match choice:
        case 1:
            colom = []
            
            for i in range(len(matrix1)):
                
                row = []
                for j in range(len(matrix1[i])):
                    if i == j:
                        sum = sum+matrix1[i][j]
                        row.append(matrix1[i][j])
                colom.append(row)
            print(colom)
            print(sum)
        case 2:
            colom = []
            
            for i in range(len(matrix1)):
                
                row = []
                for j in range(0,len(matrix1)):
                    if i == len(matrix1[i])-j-1:
                        
                        row.append(matrix1[i][j])
                        sum2 = sum2+matrix1[i][j]
                colom.append(row)
            print(colom)
            print(sum2)
        case 3 :
            if sum == 0 and sum2 == 0:
                print("Please first enter first two cases and then move to this case:")
                break
            else:
                print("Main digonal sum is :",sum)
                print("Opposite digonal sum is ",sum2)
                if sum == sum2:
                    print("Both are equal: ",sum)
                else:
                    print("Both are unequal: ")


















            
            
            
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

            
            