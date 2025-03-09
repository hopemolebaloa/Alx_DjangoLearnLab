from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "publication_year",
    )  # Fields shown in the list view
    list_filter = ("publication_year", "author")  # Filters for quick filtering
    search_fields = ("title", "author")  # Search box for titles and authors
