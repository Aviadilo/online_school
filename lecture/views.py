from rest_framework import generics, exceptions
from .serializers import *
from .models import Lecture
from rest_framework.permissions import IsAuthenticated
from .permissions import *


class LectureCreateView(generics.CreateAPIView):
    serializer_class = LectureCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.request.session['course'])
        is_course_owner = self.request.user == course.course_owner
        is_teacher = self.request.user in course.teachers.all()

        if is_course_owner or is_teacher:
            serializer.save(course=course)
        else:
            raise exceptions.PermissionDenied()


class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LectureDetailSerializer
    queryset = Lecture.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadLectureOnly)

    def get_object(self):
        obj = super().get_object()
        self.request.session['lecture'] = obj.id
        return obj
