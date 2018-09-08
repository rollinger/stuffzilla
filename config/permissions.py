from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user



class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to view and manipulate it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Permissions are allowed only to owners,
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user



class IsOwnerofUserObject(permissions.BasePermission):
    """
    Object-level permission to only allow the user object to view and manipulate it.
    Assumes the model instance is a User Model
    """
    def has_object_permission(self, request, view, obj):
        # Permissions are allowed if the obj is actually the request.user,
        # Works only on the User Model
        # O    TODO [version 0.]: Staff and Admin still can see everything...
        return obj == request.user

# O    TODO (Feature) [version 0.]: Implement Blacklist permission. see: http://www.django-rest-framework.org/api-guide/permissions/#examples
