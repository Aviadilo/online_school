from rest_framework import serializers
from .models import Lecture
from course.models import User, Course
from course.serializers import UserSerializer


class LectureCreateSerializer(serializers.ModelSerializer):
    lecture_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # course = serializers.HiddenField(default=Course.objects.get(id=1))

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

    class Meta:
        model = Lecture
        fields = '__all__'
