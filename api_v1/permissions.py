from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        # unsafe!
        return request.user.email.startswith('admin')
