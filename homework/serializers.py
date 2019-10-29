from rest_framework import serializers
from .models import Homework
from course.models import Course
from hometask.models import Hometask
from course.serializers import UserSerializer


class HomeworkCreateSerializer(serializers.ModelSerializer):
    homework_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Homework
        fields = '__all__'
        read_only_fields = ['hometask', 'mark']


class HomeworkListSerializer(serializers.ModelSerializer):
    homework_owner = UserSerializer(read_only=True)

    class Meta:
        model = Homework
        fields = ('homework_owner', 'hometask', 'homework_file', 'mark', 'created_date', 'updated_date')
