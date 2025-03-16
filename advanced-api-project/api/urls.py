from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorViewSet, BookViewSet,
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
)

# Router for ViewSets
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'viewset/books', BookViewSet)

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
    
    # Generic class-based view URLs for books
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    
    # Authentication URLs
    path('api-auth/', include('rest_framework.authtoken.urls')),
]