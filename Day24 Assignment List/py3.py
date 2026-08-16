'''
3.=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

====================================================='''


r1 = int(input("Enter Row1: "))
c1 = int(input("Enter colom 1 : "))
matrix1 = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input("Element's :")))
    matrix1.append(row)
while True:
    print("1. Count Armstrong Numbers Row-wise: ")
    print("2. Palindrome Number Column-wise: ")
    print("3. Display Average of Each Row: ")
    print("Exit: ")
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            print("Armstrong number: ")
            colom = []
            for i in range(len(matrix1)):
                row = []
            
                count=0
                for j in range(len(matrix1[i])):
                    sum = 0
                    value = matrix1[i][j]
                    temp = value
                    
                    
                    a = 0
                    while a<temp:
                        dig = temp%10
                        squ =  dig**len(str(value))
                        sum = sum +squ
                        temp = temp//10
                    if sum == matrix1[i][j]:
                        row.append(matrix1[i][j])
                        count = count+1
                    else:
                        row.append(0)
            
                        
                colom.append(row)  
                print("count of amstorng row wise: ",count)
            print(colom)
            
                                
                                    
        case 2:
            print("Plindrome Numbers Column-wise: ")
            count = 0
            add = [0]*c1
            for i in range(len(matrix1)):
                row = []
                for j in range(len(matrix1[i])):
                    Value = matrix1[i][j]
                    temp = Value
            
                    x = 0
                    rev = 0
                    while x<temp:
                        dig = temp%10
                        rev = rev*10+dig  
                        temp=temp//10
                    if rev == Value:
                        row.append(matrix1[i][j])
                        add[j] = count+1+add[j]
                    else:
                        row.append(0)
                colom.append(row)
            print(colom) 
            print(add)
        case 3:
            print("Average of Row: ")
            colom = []
            count = 0
            for i in range(len(matrix1)):
                sum = 0
                for j in range(len(matrix1[i])):
                    sum = sum + matrix1[i][j]
                avg = sum//len(matrix1)
                count = count+1
                print("Average of row: ",count,avg)
                    
        case 4:
            break
        case default :
            break
        
        



