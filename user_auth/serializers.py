from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
