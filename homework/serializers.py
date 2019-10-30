from rest_framework import serializers
from .models import Homework
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
        fields = ('homework_owner', 'hometask', 'mark', 'created_date', 'updated_date')
        read_only_fields = ['hometask', 'mark']


class HometaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hometask
        fields = ('task_body', 'possible_max_mark')


class HomeworkDetailSerializer(serializers.ModelSerializer):
    homework_owner = UserSerializer(read_only=True)
    hometask = HometaskSerializer(read_only=True)

    class Meta:
        model = Homework
        fields = ('homework_owner', 'hometask', 'homework_file', 'mark', 'created_date', 'updated_date')
        read_only_fields = ['hometask', 'mark']


class HomeworkMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('mark', )
