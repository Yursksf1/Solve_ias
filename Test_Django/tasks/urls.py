from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:task_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:task_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('polls/latest.html', views.index),
]