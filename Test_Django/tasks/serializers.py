from django.contrib.auth.models import User
from .models import Task
from rest_framework import serializers

class TaskIDSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text="ID of the task.")


class NestedTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'check', 'name', 'type_task', 'priority', 'observation', 'date_start', 'date_end')


class NestedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    #user = NestedUserSerializer(many=True, read_only=True, source='user')
    class Meta:
        model = Task
        fields = ('url', 'check', 'name', 'user', 'type_task', 'priority', 'observation', 'date_start', 'date_end')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = NestedTaskSerializer(many=True, read_only=True, source='task_set')
    class Meta:
        model = User
        fields = ( 'url', 'username', 'email', 'tasks')

