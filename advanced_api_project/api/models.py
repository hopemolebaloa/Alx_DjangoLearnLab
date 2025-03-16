from django.db import models
from django.utils import timezone

# Author model to store author details
class Author(models.Model):
    name = models.CharField(max_length=100)  # Stores the author's name

    def __str__(self):
        return self.name

# Book model with a foreign key to Author for a one-to-many relationship
class Book(models.Model):
    title = models.CharField(max_length=200)  # Stores the book's title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Links to Author

    def __str__(self):
        return f"{self.title} by {self.author.name}"