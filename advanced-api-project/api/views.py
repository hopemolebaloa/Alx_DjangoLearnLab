from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Generic views for Book model
class BookListView(generics.ListAPIView):
    """
    API view to retrieve list of books.
    Allows any user to access (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        """
        Optionally restricts the returned books by filtering
        against query parameters in the URL.
        """
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        year = self.request.query_params.get('year', None)
        
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if year is not None:
            queryset = queryset.filter(publication_year=year)
            
        return queryset

class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a specific book by ID.
    Allows any user to access (read-only).
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
    
    def perform_create(self, serializer):
        """
        Override perform_create to add additional logic when saving.
        """
        serializer.save()
        # Additional logic can be added here if needed

class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        """
        Override perform_update to add custom logic during update.
        """
        # Example: You could add logging or notifications here
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        """
        Override perform_destroy to add custom logic during deletion.
        """
        # Example: You could add logging or cleanup operations here
        instance.delete()
        
# Keep the ViewSets we had before as alternatives
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet that provides default operations for Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# We'll keep the Author views as they were...
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]