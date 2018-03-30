from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.filters import SearchFilter

from .models import Task
from .serializers import UserSerializer,  TaskSerializer, TaskIDSerializer




def index(request):
    latest_tasks_list = Task.objects.order_by('-date_start')[:5]
    context = {'latest_tasks_list': latest_tasks_list}
    return render(request, 'tasks/index.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

def results(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/results.html', {'task': task})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed, edited, or checked on.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('name', )

    @detail_route(methods=['post'], serializer_class=TaskIDSerializer)
    def check(self, request, pk=None):
        """
        API endpoint to check on an task
        """

        serializer = TaskIDSerializer(data=request.data)
        if serializer.is_valid():
            task = Task.objects.select_related('user').get(id=serializer.initial_data['id'])
            if task.user.pk == int(pk):
                if task.check:
                    task.check = False
                else:
                    task.check = True
                task.save()
            return Response({'id': task.id, 'check': task.check}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

