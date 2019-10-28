from rest_framework import serializers
from .models import Hometask
from lecture.models import Lecture


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hometask
        fields = '__all__'
        read_only_fields = ['lecture']


class LectureThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('theme',)


class TaskDetailSerializer(serializers.ModelSerializer):
    lecture = LectureThemeSerializer(read_only=True)
    class Meta:
        model = Hometask
        fields = ('lecture', 'task_body', 'possible_max_mark')
