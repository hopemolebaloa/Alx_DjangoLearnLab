from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer serializes the Book model.
    It includes custom validation to ensure the publication_year is not in the future.
    """
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    def validate_publication_year(self, value):
        """
        Validate that publication_year is not in the future.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(f'Publication year cannot be in the future. Current year is {current_year}.')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes the Author model.
    It includes a nested representation of all books by this author using the BookSerializer.
    This demonstrates handling of one-to-many relationships in DRF.
    """
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']