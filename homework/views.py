from rest_framework import generics, filters
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django.shortcuts import get_object_or_404


class HomeworkCreateView(generics.CreateAPIView):
    serializer_class = HomeworkCreateSerializer
    permission_classes = (IsAuthenticated, IsStudent)

    def perform_create(self, serializer):
        task_id = self.request.session.get('task')
        task = get_object_or_404(Hometask, id=task_id)
        serializer.save(hometask=task)


class HomeworkListView(generics.ListAPIView):
    serializer_class = HomeworkListSerializer
    permission_classes = (IsAuthenticated, IsTeacher)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['homework_owner__username']
    ordering_fields = ['mark']

    def get_queryset(self):
        task_id = self.request.session.get('task')
        task = get_object_or_404(Hometask, id=task_id)
        return Homework.objects.filter(hometask=task).order_by('mark')


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
        homework_id = self.request.session.get('homework')
        homework = get_object_or_404(Homework, id=homework_id)
        serializer.save(homework=homework)
