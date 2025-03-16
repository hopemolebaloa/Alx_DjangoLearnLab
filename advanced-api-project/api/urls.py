from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorViewSet, BookViewSet,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
)

# REST Framework router
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

# URL patterns for both API and traditional views
urlpatterns = [
    # REST API URLs
    path('api/', include(router.urls)),
    
    # Traditional Django URLs for Authors
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/new/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    
    # Traditional Django URLs for Books
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Changed from 'new' to 'create'
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # Changed format
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # Changed format
]