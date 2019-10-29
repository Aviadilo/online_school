from rest_framework import generics
from .serializers import *
from .models import Course
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django.db.models import Q


class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer
    permission_classes = (IsAuthenticated,)


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadCourseOnly)

    def get_object(self):
        obj = super().get_object()
        self.request.session['course'] = obj.id
        return obj


class CourseUsersView(generics.RetrieveUpdateAPIView):
    serializer_class = CourseUsersSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadCourseOnly)


class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadCourseOnly)

    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(Q(course_owner=user) |
                                     Q(students=user) |
                                     Q(teachers=user)).order_by('name')
