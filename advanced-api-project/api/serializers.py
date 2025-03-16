from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer serializes the Book model with enhanced validation.
    """
    author_name = serializers.ReadOnlyField(source='author.name')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'author_name']
        
    def validate_publication_year(self, value):
        """
        Check that the publication year is not in the future and not too far in the past.
        """
        current_year = timezone.now().year
        
        if value > current_year:
            raise serializers.ValidationError(f"Publication year cannot be in the future. Current year is {current_year}.")
            
        if value < 1700:  # Arbitrary cutoff for illustration
            raise serializers.ValidationError("Publication year seems suspiciously old. Please verify.")
            
        return value
        
    def validate_title(self, value):
        """
        Check that the title is not too short and doesn't contain inappropriate content.
        """
        if len(value) < 3:
            raise serializers.ValidationError("Book title must be at least 3 characters long.")
            
        forbidden_words = ["spam", "inappropriate", "offensive"]  # Example list
        for word in forbidden_words:
            if word in value.lower():
                raise serializers.ValidationError(f"Book title contains inappropriate content: '{word}'")
                
        return value
        
    def validate(self, data):
        """
        Cross-field validation example.
        """
        if 'title' in data and 'publication_year' in data:
            # Example: Books published before 1900 shouldn't have "Modern" in title
            if data['publication_year'] < 1900 and "Modern" in data['title']:
                raise serializers.ValidationError(
                    "Books published before 1900 shouldn't have 'Modern' in the title."
                )
        return data

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes the Author model.
    It includes a nested representation of books by this author.
    """
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        
    def validate_name(self, value):
        """
        Check that the author name is properly formatted.
        """
        if len(value) < 2:
            raise serializers.ValidationError("Author name must be at least 2 characters long.")
            
        # Check that name doesn't contain numbers
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Author name should not contain numbers.")
            
        return value