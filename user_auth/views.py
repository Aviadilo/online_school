from rest_framework import generics
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserLoginView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = UserLoginSerializer

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
