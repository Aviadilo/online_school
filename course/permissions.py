from rest_framework import permissions
from .models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_owner = obj.course_owner == request.user
        is_teacher = request.user in obj.teachers.all()
        is_student = request.user in obj.students.all()
        if request.method in permissions.SAFE_METHODS:
            return is_owner or is_teacher or is_student
        return is_owner
