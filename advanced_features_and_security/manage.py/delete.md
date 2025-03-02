# Delete Operation

## Command:
```python
from bookshelf.models import Book  # Missing import statement added

# Retrieve the book with title "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
books = Book.objects.all()
print(list(books))

