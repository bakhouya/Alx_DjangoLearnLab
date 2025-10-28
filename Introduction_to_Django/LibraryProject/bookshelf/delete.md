# delete item book where title = Nineteen Eighty-Four and get all books 

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
#  (1, {'bookshelf.Book': 1})

Book.objects.all()
#  <QuerySet []>
