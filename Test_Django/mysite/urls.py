"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#from django.urls import include, path
#from django.contrib import admin
#from django.contrib.auth import views as auth_views


#urlpatterns = [
#    path('', include('tasks.urls')),
#    path('admin/', admin.site.urls),
#    path('accounts/login/', auth_views.LoginView.as_view()),
    #path('api-auth/', include('rest_framework.urls'))
#]

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from tasks import views


router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)


API_TITLE = 'tasks API'
API_DESCRIPTION = 'A demo of the Task Examples implementing DRF'

urlpatterns = [
    url(r'^$', view=TemplateView.as_view(template_name='tasks/index.html')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]