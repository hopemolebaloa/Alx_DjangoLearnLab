# accounts/urls.py
from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]

# social_media_api/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
]

# Add media URL if profile pictures are being used
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)