# Update item book where title = 1984 to New title = Nineteen Eighty-Four

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

### Nineteen Eighty-Four
