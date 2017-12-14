from rest_framework.permissions import BasePermission


class CanChangeProfile(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.has_perm('rucken_todo.change_profile')
