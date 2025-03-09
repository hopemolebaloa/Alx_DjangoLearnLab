from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book details"),
            ("can_create", "Can add a new book"),
            ("can_edit", "Can edit an existing book"),
            ("can_delete", "Can delete a book"),
        ]

    def __str__(self):
        return self.title
