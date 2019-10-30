from rest_framework import generics
from .models import User
from .serializers import UserCreateSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
