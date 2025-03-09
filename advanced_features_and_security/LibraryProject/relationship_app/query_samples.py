import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Corrected query
        return books
    except Author.DoesNotExist:
        return "Author not found."


# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return "Library not found."


# ✅ Query 3: Retrieve the librarian for a library (FIXED)
def get_librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # <-- Required query
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return "Library or Librarian not found."


if __name__ == "__main__":
    # Sample Data Insertion
    author = Author.objects.create(name="George Orwell")
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    librarian = Librarian.objects.create(name="John Doe", library=library)

    # Running queries
    print("Books by George Orwell:", list(get_books_by_author("George Orwell")))
    print("Books in Central Library:", list(get_books_in_library("Central Library")))
    print("Librarian of Central Library:", get_librarian_of_library("Central Library"))
