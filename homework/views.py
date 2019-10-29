from rest_framework import generics, exceptions
from .serializers import *
from .models import Homework
from hometask.models import Hometask
from rest_framework.permissions import IsAuthenticated
from .permissions import *


class HomeworkCreateView(generics.CreateAPIView):
    serializer_class = HomeworkCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        task = Hometask.objects.get(id=self.request.session['task'])
        if self.request.user in task.lecture.course.students.all():
            serializer.save(hometask=task)
        else:
            raise exceptions.PermissionDenied()


class HomeworkListView(generics.ListAPIView):
    serializer_class = HomeworkListSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Homework.objects.all()

    def get_queryset(self):
        task = Hometask.objects.get(id=self.request.session['task'])
        is_course_owner = self.request.user == task.lecture.course.course_owner
        is_teacher = self.request.user in task.lecture.course.teachers.all()
        if is_course_owner or is_teacher:
            return Homework.objects.filter(hometask=task)
        else:
            raise exceptions.PermissionDenied()
