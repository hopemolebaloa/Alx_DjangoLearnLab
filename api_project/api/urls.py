from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # List books (authenticated users)
    path('', include(router.urls)),  # CRUD operations (admin users)
    path('token/', obtain_auth_token, name='api_token_auth'),  # Get token via username/password
]