# Delete Operation
## Command:
```python
# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(list(books))
