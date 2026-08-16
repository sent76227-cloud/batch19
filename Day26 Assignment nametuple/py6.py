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

book = namedtuple("Book", ["book_id", "title", "author", "price"])

n = int(input("Enter number of books: "))

books = []

# 1. Read book records
for i in range(n):
    book_id, title, author, price = input().split()

    b = book(book_id, title, author, int(price))
    books.append(b)


# 2. Display all book details
print("\nAll Books:")

for b in books:
    print(b.book_id, b.title, b.author, b.price)


# 3. Find most expensive book
expensive = books[0]

for b in books:
    if b.price > expensive.price:
        expensive = b

print("\nMost Expensive Book:")
print(expensive.book_id, expensive.title, expensive.author, expensive.price)


# 4. Calculate average price
total = 0

for b in books:
    total += b.price

average = total / n

print("\nAverage Book Price:")
print(average)


# 5. Search books by author
search_author = input("\nEnter Author Name: ")

print("\nBooks Written By", search_author + ":")

for b in books:
    if b.author == search_author:
        print(b.book_id, b.title, b.author, b.price)