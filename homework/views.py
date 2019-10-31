from rest_framework import generics
from .serializers import *
from .models import Homework
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django.shortcuts import get_object_or_404


class HomeworkCreateView(generics.CreateAPIView):
    serializer_class = HomeworkCreateSerializer
    permission_classes = (IsAuthenticated, IsStudent)

    def perform_create(self, serializer):
        task = get_object_or_404(Hometask, id=self.request.session['task'])
        serializer.save(hometask=task)


class HomeworkListView(generics.ListAPIView):
    serializer_class = HomeworkListSerializer
    permission_classes = (IsAuthenticated, IsTeacher)
    queryset = Homework.objects.all()

    def get_queryset(self):
        task = get_object_or_404(Hometask, id=self.request.session['task'])
        return Homework.objects.filter(hometask=task)


class HomeworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkDetailSerializer
    queryset = Homework.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadHomeworkOnly)

    def get_object(self):
        obj = super().get_object()
        self.request.session['homework'] = obj.id
        return obj


class HomeworkMarkDetailView(generics.UpdateAPIView):
    serializer_class = HomeworkMarkSerializer
    queryset = Homework.objects.all()
    permission_classes = (IsAuthenticated, IsTeacher)


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated, IsTeacherOrHomeworkOwner)

    def perform_create(self, serializer):
        homework = get_object_or_404(Homework, id=self.request.session['homework'])
        serializer.save(homework=homework)
