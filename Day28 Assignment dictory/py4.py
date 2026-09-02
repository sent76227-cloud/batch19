'''4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

--- '''
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

hig = 1
low = 100
for k,v in students.items():
    print(v)
    if hig < v:
        hig = v
        print(hig)
    if low > v:
        low = v
for k , v in students.items():
    if v ==  hig :
        print(k,"Higest markes: ",hig)
    if v == low:    
        print(k,"Lowest marks:",low)
        