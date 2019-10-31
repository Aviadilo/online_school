from rest_framework import permissions
from django.shortcuts import get_object_or_404
from hometask.models import Hometask
from homework.models import Homework


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        task = get_object_or_404(Hometask, id=request.session['task'])
        is_student = request.user in task.lecture.course.students.all()
        return is_student


class IsOwnerOrReadHomeworkOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_homework_owner = request.user == obj.homework_owner
        is_teacher = request.user in obj.hometask.lecture.course.teachers.all()

        if request.method in permissions.SAFE_METHODS:
            return is_homework_owner or is_teacher
        return is_homework_owner


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        task = get_object_or_404(Hometask, id=request.session['task'])
        is_teacher = request.user in task.lecture.course.teachers.all()

        return is_teacher


class IsTeacherOrHomeworkOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        homework = get_object_or_404(Homework, id=request.session['homework'])
        is_teacher = request.user in homework.hometask.lecture.course.teachers.all()
        is_homework_owner = request.user == homework.homework_owner

        return is_teacher or is_homework_owner
