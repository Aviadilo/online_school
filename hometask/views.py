from rest_framework import generics
from .serializers import *
from .models import Hometask
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django.shortcuts import get_object_or_404


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated, IsTeacher)

    def perform_create(self, serializer):
        lecture_id = self.request.session.get('lecture')
        lecture = get_object_or_404(Lecture, id=lecture_id)
        serializer.save(lecture=lecture)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    queryset = Hometask.objects.all()
    permission_classes = (IsAuthenticated, IsTeacherOrReadTaskOnly)

    def get_object(self):
        obj = super().get_object()
        self.request.session['task'] = obj.id
        return obj
