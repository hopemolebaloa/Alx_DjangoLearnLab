# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'follower_count')
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('bio', 'profile_picture', 'followers')}),
    )

admin.site.register(User, CustomUserAdmin)
