from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books



def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()




def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian
