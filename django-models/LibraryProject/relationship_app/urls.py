from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path("add-book/", add_book, name="add_book"),
    path("edit-book/<int:book_id>/", edit_book, name="edit_book"),
    path("delete-book/<int:book_id>/", delete_book, name="delete_book"),
]






