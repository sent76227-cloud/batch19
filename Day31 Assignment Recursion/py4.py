'''Assignment 4:
 Lottery Ticket Verification (Count Occurrences Using Recursion)

A lottery company assigns a unique ticket number to every participant. Before announcing the results, the company wants to determine how many times a lucky digit appears in a ticket number. This helps identify tickets eligible for special bonus rewards.

As a software developer, your task is to write a recursive Python program that counts the number of times a given digit appears in the ticket number.

Task

Write a recursive function to count the occurrences of a given digit in a ticket number.

Input Format
The first line contains an integer representing the Ticket Number.
The second line contains an integer representing the Lucky Digit.
Output Format

Display the number of times the lucky digit appears in the ticket number using the format:

Digit <Lucky Digit> appears <Count> times.
Sample Input
Enter Ticket Number:
1122334412

Enter Lucky Digit:
2
Sample Output
Digit 2 appears 3 times.
Sample Input 2
Enter Ticket Number:
987654321

Enter Lucky Digit:
5
Sample Output 2
Digit 5 appears 1 time.
Sample Input 3
Enter Ticket Number:
11111111

Enter Lucky Digit:
2
Sample Output 3
Digit 2 appears 0 times.
'''
count = 0
def ticket_nu(lucky,number):
    
    if number == 0:
        return  0
    check = number%10
    if check ==  lucky:
        return 1 + ticket_nu(lucky,number//10)
    else:
        return 0 + ticket_nu(lucky,number//10)
print(ticket_nu(2,1223232))