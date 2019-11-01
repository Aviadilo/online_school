from rest_framework import permissions
from course.models import Course
from django.shortcuts import get_object_or_404


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        course_id = request.session.get('course')
        course = get_object_or_404(Course, id=course_id)
        is_teacher = request.user in course.teachers.all()

        return is_teacher


class IsTeacherOrReadLectureOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_teacher = request.user in obj.course.teachers.all()
        is_student = request.user in obj.course.students.all()

        if request.method in permissions.SAFE_METHODS:
            return is_teacher or is_student
        return is_teacher
