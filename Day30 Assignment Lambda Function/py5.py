'''
QNO 5:
Employee Data Processing System

A company stores information about its employees in two forms:

A list of employee ages.
A string containing employee names separated by spaces.

The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

Problem Statement

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.
Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.
Menu

====================================================
Enter your choice:
Sample Input
Employee Ages:
34 55 29 60 55 42 60 51

Employee Names:
Ajay Rahul Esha Omkar Ishita Neha
Sample Output
Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita
Instructions
Implement all operations using separate functions.
Each function must accept parameters and return the result.
Do not print results inside the functions.
The menu should continue to appear until the user selects Exit.
Display an appropriate message for an invalid choice.
Use meaningful function and variable names and follow proper indentation'''
age =  list(map(int,input("Enter age: ").split()))
empname = []
for i in range(len(age)):
    empname.append(input("enter name: "))
print(age)
print(empname)


while True:
    print("========== EMPLOYEE DATA PROCESSING SYSTEM ==========")
    print("1. Find Second Highest Employee Age")
    print("2. Count Senior Employees")
    print("3. Remove Duplicate Ages")
    print("4. Count Names Starting with a Vowel")
    print("5. Find Longest Employee Name")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            print("1. Find Second Highest Employee Age")
            max =  age[0]
            sec_max  = age[0]
            for i in range(len(age)):
                if age[i]>max:
                    sec_max = max
                    max = age[i]
            
            print("Second largest: ",sec_max)




            
        case 2:
            print("Count senior employes:  ")
            result = list(filter(lambda x:x>=50,age)) 
            print(len(result))
        case 3 :
            print("Remove duplicate age")
            change = set(age)
            print(change)
        case 4:
            print("count name start with vovel")
            result = list(filter(lambda x:x[0] in "aeiou",empname))
            print(result)
        case 5 :
            print("Find longest name of empoyes: ")
            emplen = len(empname[0])
            for i in range(len(empname)):
                if len(i)>emplen:
                    emplen = len(i)
            print(emplen)
        case 6:
            print("Use for Quit")
            break
        case _:
            break
print("You are out of loop")