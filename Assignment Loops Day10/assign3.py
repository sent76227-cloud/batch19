''' 3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35 '''   

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

count = 1
for i in range(num1,num2+1):
   count= count+1
   if count%2!=0:
           table = count*5
           if table > num1:
                 if num2 < table:
                     break
                 else:
                     print(table, end= " ")



           
           
   


