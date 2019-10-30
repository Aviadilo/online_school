from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.serializers import CharField, ValidationError


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    username = CharField()

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = authenticate(**validated_data)
        if user is not None:
            login(self.context['request'], user=user)
            return user
        else:
            raise ValidationError('Incorrect credentials')
