from rest_framework import permissions
from course.models import Course


class IsOwnerOrTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        course = Course.objects.get(id=request.session['course'])
        is_course_owner = course.course_owner == request.user
        is_teacher = request.user in course.teachers.all()

        return is_course_owner or is_teacher


class IsOwnerOrReadLectureOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_lecture_owner = request.user == obj.lecture_owner
        is_course_owner = request.user == obj.course.course_owner
        is_teacher = request.user in obj.course.teachers.all()
        is_student = request.user in obj.course.students.all()

        if request.method in permissions.SAFE_METHODS:
            return is_course_owner or is_teacher or is_student
        return is_lecture_owner
