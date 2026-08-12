'''3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times '''


review = input("Enter product review: ")
char = input("Enter character to check: ")
count = 0

length = len(review)
i = 0
while i < length:
      ch = review[i]
      if ch == char:
          count=count+1
      i = i+1
print(f"Total {char} occurs: {count} ")