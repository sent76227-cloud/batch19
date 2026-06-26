
'''10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3 '''


num = int(input("Enter number: "))
count = 0
i = 1
while num > 0:
   dig = num%10
   if dig%2 != 0:
       #print(dig,end = " " )
       count = count + 1
   num = num//10
 
print(count)






