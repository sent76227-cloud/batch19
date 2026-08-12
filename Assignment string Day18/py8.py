'''
8.
Airport Passenger Name Formatting System

An international airport is developing an automated passenger management system. Many passengers enter their details in different formats such as lowercase, uppercase, mixed-case letters, and numbers while booking flight tickets online.

Due to inconsistent formatting, problems occur while generating boarding passes, security verification records, and passenger identity reports.

To solve this issue, the airport authority wants a program that automatically converts only the first character of every word into uppercase while keeping all remaining characters unchanged.

The input may contain:
- Passenger names
- Passport details
- Terminal names
- Seat numbers
- City names
- Mixed uppercase/lowercase letters
- Digits

Task:
Read a complete string from the user and convert the first character of every word into uppercase.

Conditions:
- Words may contain spaces
- Digits should remain unchanged
- Do not use built-in title() function

Input:
Enter passenger details:
deepika padukone flight ai202 terminal 3 mumbai

Output:
Formatted Details:
Deepika Padukone Flight Ai202 Terminal 3 Mumbai


Test Case 2:
Input:
Enter passenger details:
DEEPIKA pADukone gate number 12

Output:
Formatted Details:
DEEPIKA PADukone Gate Number 12


Test Case 3:
Input:
Enter passenger details:
international departure terminal delhi airport

Output:
Formatted Details:
International Departure Terminal Delhi Airport


Test Case 4:
Input:
Enter passenger details:
business class passenger seat b12

Output:
Formatted Details:
Business Class Passenger Seat B12


'''




infor = input("Enter Passenger details: ")
a = 0


length = len(infor)
i = 0
while i < length:
     ch = infor[i]
     if i == 0:
        if ch >= "a" and ch <= "z":
            infor = infor[:i] + chr(ord(ch)-32) + infor[i+1:]
        
     elif a == 1:
           if ch >= "a" and ch <= "z":
              infor = infor[:i] + chr(ord(ch)-32) + infor[i+1:]
           a = 0
     elif ch == " ":
          
          a = 1
            
     i = i+1
print("Formatted Information: ")
print(infor)
































'''
first = input("Enter First Product Code: ").lower()
second = input("Enter Second Product Code: ").lower()
firstlen = len(first)
secondlen = len(second)
i = 0
match = True 
while i < firstlen:
    ch = first[i]
    if ch == " ":
         i = i+1
         continue
   
    j = 0
    found = False
    while j < secondlen:
             sch = second[j]
             if sch == " ":
                 j = j+1
                 continue
             elif ch == sch:
                  second = second[:j] + "*" +  second[j+1:]
                  found = True
                  break
             j = j+1
    if found == False:
          match = False
          break
    i = i+1  
j = 0
while j < secondlen:
      if second[j] != " " and second[j] != "*":
              match =  False
              break
      j = j+1
if match:
    print("Both Product codes are matching")
else:    
    print("Both product codes are not matching")
'''





             