from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # For this example, let's assume that if the object has an author field,
        # we check if the request.user is the author. Otherwise, we use a different field.
        if hasattr(obj, 'author'):
            return obj.author.id == request.user.id
        return False