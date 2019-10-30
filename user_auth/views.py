from rest_framework import generics
from .serializers import UserCreateSerializer, UserLoginSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
