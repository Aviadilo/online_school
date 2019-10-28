from rest_framework import permissions


class IsOwnerOrReadTaskOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_lecture_owner = request.user == obj.lecture.lecture_owner
        is_teacher = request.user in obj.lecture.course.teachers.all()
        is_student = request.user in obj.lecture.course.students.all()

        if request.method in permissions.SAFE_METHODS:
            return is_lecture_owner or is_teacher or is_student
        return is_lecture_owner
