from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# View Book Details (Restricted to users with 'can_view' permission)
@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/view_books.html", {"books": books})

# Add a Book (Restricted to users with 'can_create' permission)
@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

# Edit a Book (Restricted to users with 'can_edit' permission)
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("view_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

# Delete a Book (Restricted to users with 'can_delete' permission)
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("view_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})

# View to list all books (Requires 'can_view' permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    This view allows users to see the list of books.
    Only users with 'can_view' permission can access this page.
    """
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

