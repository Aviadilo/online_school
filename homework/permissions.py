from rest_framework import permissions


class IsOwnerOrReadHomeworkOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_homework_owner = request.user == obj.homework_owner
        is_teacher = request.user in obj.hometask.lecture.course.teachers.all()
        is_course_owner = request.user == obj.hometask.lecture.course.course_owner

        if request.method in permissions.SAFE_METHODS:
            return is_homework_owner or is_course_owner or is_teacher
        return is_homework_owner


class IsTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_teacher = request.user in obj.hometask.lecture.course.teachers.all()

        return is_teacher
