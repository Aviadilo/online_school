from rest_framework import permissions
from lecture.models import Lecture


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        lecture = Lecture.objects.get(id=request.session['lecture'])
        is_teacher = request.user in lecture.course.teachers.all()

        return is_teacher


class IsTeacherOrReadTaskOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_teacher = request.user in obj.lecture.course.teachers.all()
        is_student = request.user in obj.lecture.course.students.all()

        if request.method in permissions.SAFE_METHODS:
            return is_teacher or is_student
        return is_teacher
