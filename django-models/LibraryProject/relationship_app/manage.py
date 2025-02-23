from django.contrib.auth.models import User
from relationship_app.models import UserProfile

# Create a test user
user = User.objects.create_user(username="admin_user", password="admin123")
user.userprofile.role = "Admin"
user.userprofile.save()

librarian = User.objects.create_user(username="librarian_user", password="librarian123")
librarian.userprofile.role = "Librarian"
librarian.userprofile.save()

member = User.objects.create_user(username="member_user", password="member123")
member.userprofile.role = "Member"
member.userprofile.save()
