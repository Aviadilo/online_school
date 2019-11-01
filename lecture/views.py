from rest_framework import generics
from .serializers import *
from .models import Lecture
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django.shortcuts import get_object_or_404


class LectureCreateView(generics.CreateAPIView):
    serializer_class = LectureCreateSerializer
    permission_classes = (IsAuthenticated, IsTeacher)

    def perform_create(self, serializer):
        course_id = self.request.session.get('course')
        course = get_object_or_404(Course, id=course_id)
        serializer.save(course=course)


class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LectureDetailSerializer
    queryset = Lecture.objects.all()
    permission_classes = (IsAuthenticated, IsTeacherOrReadLectureOnly)

    def get_object(self):
        obj = super().get_object()
        self.request.session['lecture'] = obj.id
        return obj
