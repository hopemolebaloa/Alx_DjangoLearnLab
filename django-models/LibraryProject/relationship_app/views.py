from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

# Role check function for Member
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Member"

# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")




