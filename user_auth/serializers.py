from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.serializers import (EmailField, CharField, ValidationError)


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

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user is not None:
            return attrs
        else:
            raise ValidationError('Incorrect credentials')
