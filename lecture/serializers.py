from rest_framework import serializers
from .models import Lecture
from course.models import Course
from course.serializers import UserSerializer


class LectureCreateSerializer(serializers.ModelSerializer):
    lecture_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lecture
        fields = '__all__'
        read_only_fields = ['course']


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name',)


class LectureDetailSerializer(serializers.ModelSerializer):
    lecture_owner = UserSerializer(read_only=True)
    course = CourseNameSerializer(read_only=True)
    lecture_tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Lecture
        fields = ('lecture_owner', 'course', 'theme', 'lecture_file', 'lecture_tasks', 'created_date')
