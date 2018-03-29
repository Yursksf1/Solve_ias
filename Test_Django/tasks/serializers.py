from django.contrib.auth.models import User
from .models import Task
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('check', 'name', 'user', 'type_task', 'priority', 'observation', 'date_start', 'date_end')

