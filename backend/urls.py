"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from backend import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

#from backend.views import ToDoListView, ToDoDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/',views.quiz.as_view()),
    url(r'^auth/',views.authentication.as_view()),
    #url(r'^api/v1/auth/',include('rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
    #url(r'^$',views.IndexView.as_view(),name='index'),
    #url(r'^$', TemplateView.as_view(template_name='backend/index.html')),
 ]
urlpatterns=format_suffix_patterns(urlpatterns)