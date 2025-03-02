ffrom django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

# Get content type for Book model
content_type = ContentType.objects.get_for_model(Book)

# Define permissions
add_perm = Permission.objects.get(codename="can_add_book", content_type=content_type)
change_perm = Permission.objects.get(codename="can_change_book", content_type=content_type)
delete_perm = Permission.objects.get(codename="can_delete_book", content_type=content_type)

# Assign permissions to a user (Example: admin)
user = User.objects.get(username="admin_user")
user.user_permissions.add(add_perm, change_perm, delete_perm)
user.save()

