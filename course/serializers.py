from rest_framework import serializers
from .models import Course
from lecture.models import Lecture
from user_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CourseCreateSerializer(serializers.ModelSerializer):
    course_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'theme')


class CourseDetailSerializer(serializers.ModelSerializer):
    course_owner = UserSerializer(read_only=True)
    course_lectures = LectureSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('course_owner', 'name', 'course_lectures', 'created_date', 'updated_date')


class CourseUsersSerializer(serializers.ModelSerializer):
    course_owner = UserSerializer(read_only=True)
    teachers = UserSerializer(many=True)
    students = UserSerializer(many=True)

    class Meta:
        model = Course
        fields = ('course_owner', 'teachers', 'students')


class CourseListSerializer(serializers.ModelSerializer):
    course_owner = UserSerializer()

    class Meta:
        model = Course
        fields = ('id', 'course_owner', 'name', 'created_date')
