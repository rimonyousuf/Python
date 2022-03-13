books=[]
books.append("C programming Book")
books.append("C++ programming Book")
books.append("Java programming Book")

print(books)

books.pop()
print("Now the top book is",books[-1])

books.pop()
print("Now the top book is",books[-1])

books.pop()
if not books:
    print("No books")