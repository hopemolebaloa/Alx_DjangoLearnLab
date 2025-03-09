from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer

# Keep the existing BookList view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Add the new BookViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
