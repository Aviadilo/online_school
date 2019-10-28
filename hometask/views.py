from rest_framework import generics, exceptions
from .serializers import *
from .models import Hometask
from rest_framework.permissions import IsAuthenticated
from .permissions import *


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        lecture = Lecture.objects.get(id=self.request.session['lecture'])

        if self.request.user == lecture.lecture_owner:
            serializer.save(lecture=lecture)
        else:
            raise exceptions.PermissionDenied()


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    queryset = Hometask.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadTaskOnly)

    def get_object(self):
        obj = super().get_object()
        self.request.session['task'] = obj.id
        return obj
