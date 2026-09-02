'''QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''
from collections import namedtuple
books = namedtuple("field",["book_id", "title", "author", "price"])
n = int(input("Enter book number: "))
l = []

for i in range(n):
    
    id = int(input("Enter id of book: "))
    t = input("Enter title of book: ")
    aut = input("Enter author name: ")
    pri = int(input("Enter price :"))
    a = books(id,t,aut,pri)
    l.append(a)
for i in l:
    print(i.book_id ,"And",i.title,"And",i.author,"And",i.price)
expenc = l[0].price
for i in l:
    if expenc < i.price:
        expenc = i.price
print("Expencve: ",expenc)
author_name = input("Enter author name")
for i in l:
    if i.author == author_name:
        print("Book name : ",i.title)
    
    

