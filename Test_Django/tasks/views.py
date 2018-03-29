from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Task
from django.urls import reverse



#def index(request):
#    latest_tasks_list = Task.objects.order_by('-date_start')[:5]
#    context = {'latest_tasks_list': latest_tasks_list}
#    return render(request, 'tasks/index.html', context)


#def detail(request, task_id):
#    task = get_object_or_404(Task, pk=task_id)
#    return render(request, 'tasks/detail.html', {'task': task})

#def results(request, task_id):
#    task = get_object_or_404(Task, pk=task_id)
#    return render(request, 'tasks/results.html', {'task': task})

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tasks.serializers import UserSerializer,  TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer