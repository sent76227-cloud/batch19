from models.book import Book

books = []
for _ in range(5):
    book_id = int(input("Enter Book ID: "))
    book_name = input("Enter Book Name: ")
    author = input("Enter Author: ")
    price = int(input("Enter Price: "))
    books.append(Book(book_id, book_name, author, price))

print("\nAll Books:")
for book in books:
    book.display()

search_id = int(input("\nEnter Book ID to search: "))
found = None
for book in books:
    if book.book_id == search_id:
        found = book
        break
if found:
    print("Book Found:")
    found.display()
else:
    print("Book not found")

author_name = input("\nEnter author name to filter books: ")
print(f"Books by {author_name}:")
for book in books:
    if book.author == author_name:
        print(f"{book.book_id} {book.book_name} {book.price}")

print("\nBooks with price greater than 500:")
for book in books:
    if book.price > 500:
        print(book.book_name)

most_expensive = max(books, key=lambda b: b.price)
print(f"\nMost Expensive Book: {most_expensive.book_name} = {most_expensive.price}")

average_price = sum(book.price for book in books) / len(books)
print(f"\nAverage Price: {average_price}")
