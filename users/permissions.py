from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'Admin':
            return True
        return False

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'Teacher':
            return True
        return False