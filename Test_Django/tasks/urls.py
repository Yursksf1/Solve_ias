from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

#app_name = 'tasks'
urlpatterns = [
    url(r'^api/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:task_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:task_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('polls/latest.html', views.index),
]