from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# REST Framework ViewSets
class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Author instances via API.
    Includes nested serialization of related books.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Book instances via API.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Traditional Django Class-Based Views for Authors
class AuthorListView(ListView):
    """
    View for displaying a list of all authors.
    """
    model = Author
    template_name = 'api/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    """
    View for displaying details of a specific author.
    """
    model = Author
    template_name = 'api/author_detail.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    """
    View for creating a new author.
    """
    model = Author
    template_name = 'api/author_form.html'
    fields = ['name']
    success_url = reverse_lazy('author-list')

class AuthorUpdateView(UpdateView):
    """
    View for updating an existing author.
    """
    model = Author
    template_name = 'api/author_form.html'
    fields = ['name']
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(DeleteView):
    """
    View for deleting an author.
    """
    model = Author
    template_name = 'api/author_confirm_delete.html'
    success_url = reverse_lazy('author-list')

# Traditional Django Class-Based Views for Books
class BookListView(ListView):
    """
    View for displaying a list of all books.
    """
    model = Book
    template_name = 'api/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    """
    View for displaying details of a specific book.
    """
    model = Book
    template_name = 'api/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    """
    View for creating a new book.
    """
    model = Book
    template_name = 'api/book_form.html'
    fields = ['title', 'publication_year', 'author']
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    """
    View for updating an existing book.
    """
    model = Book
    template_name = 'api/book_form.html'
    fields = ['title', 'publication_year', 'author']
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    """
    View for deleting a book.
    """
    model = Book
    template_name = 'api/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')