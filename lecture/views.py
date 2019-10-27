from rest_framework import generics
from .serializers import *
from .models import Lecture
from rest_framework.permissions import IsAuthenticated
from .permissions import *


class LectureCreateView(generics.CreateAPIView):
    serializer_class = LectureCreateSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrTeacher)

    def perform_create(self, serializer):
        serializer.save(course=Course.objects.get(id=self.request.session['course']))


class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LectureDetailSerializer
    queryset = Lecture.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadLectureOnly)

    def get_object(self):
        obj = super().get_object()
        self.request.session['lecture'] = obj.id
        return obj
