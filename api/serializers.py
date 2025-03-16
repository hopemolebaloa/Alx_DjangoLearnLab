from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

# Serializer for the Author model, including nested Book data
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication_year is not in the future.
        """
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# The relationship between Author and Book is handled by nesting BookSerializer 
# in AuthorSerializer, allowing dynamic serialization of all books for an author.
# The one-to-many relationship is reflected with many=True in the books field.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def __str__(self):
        return self.name