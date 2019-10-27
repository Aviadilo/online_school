from rest_framework import serializers
from .models import Course, User


class UserSerializer(serializers.ModelSerializer):
    # teacher_courses = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        # fields = ('id', 'username', 'teacher_courses')
        fields = ('username',)


class CourseCreateSerializer(serializers.ModelSerializer):
    course_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    course_owner = UserSerializer(read_only=True)
    course_lectures = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('course_owner', 'name', 'course_lectures', 'created_date', 'updated_date')
        # extra_kwargs = {
        #     'course_owner': {'read_only': True},
        # }
        # read_only_fields = ['course_lectures']


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
        fields = ('course_owner', 'name', 'created_date')
