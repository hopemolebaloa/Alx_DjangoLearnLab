from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .filters import BookFilter

# Updated BookListView with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    """
    API view to retrieve list of books with filtering, searching and ordering capabilities.
    
    Filtering:
    - Filter by title: ?title=django
    - Filter by publication_year: ?publication_year=2023
    - Filter by author ID: ?author=1
    - Filter by author name: ?author_name=tolkien
    - Filter by publication year range: ?min_year=2000&max_year=2023
    
    Searching:
    - Search across title and author name: ?search=python
    
    Ordering:
    - Order by any field: ?ordering=publication_year
    - Reverse ordering: ?ordering=-publication_year
    - Multiple ordering fields: ?ordering=author__name,publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    # Configure filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Set up filterset class for advanced filtering
    filterset_class = BookFilter
    
    # Set up fields for basic searching
    search_fields = ['title', 'author__name']
    
    # Set up fields for ordering
    ordering_fields = ['title', 'publication_year', 'author__name']
    
    # Default ordering
    ordering = ['publication_year']

# Keep other views from previous implementation
class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a specific book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Update ViewSet to include filtering as well
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet that provides default operations for Book model.
    Includes filtering, searching and ordering capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['publication_year']

# Author ViewSet with filtering capabilities
class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Author instances.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']