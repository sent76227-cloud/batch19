''' 1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3 '''

a = list(map(int,input("Enter Student marks: ").split()))
hig = a[0]
low  = a[0]
count  = 0
for i in a:
    if i > hig :
        hig = i
    if i < low :
        low = i
    if i > 75:
        count = count+1
print(a,"-> Highest ",hig,"Lowest = ",low,"count above = ",count)






