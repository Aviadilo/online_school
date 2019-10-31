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
        fields = ('id', 'homework_owner', 'hometask', 'mark', 'created_date', 'updated_date')
        read_only_fields = ['id', 'hometask', 'mark']


class HometaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hometask
        fields = ('id', 'task_body', 'possible_max_mark')


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

    def validate(self, attrs):
        homework_id = self.context['request'].session['homework']
        max_mark = Homework.objects.values('hometask__possible_max_mark').get(id=homework_id)['hometask__possible_max_mark']
        if attrs['mark'] > max_mark:
            raise serializers.ValidationError("Mark cannot be more than {}".format(max_mark))
        return attrs
