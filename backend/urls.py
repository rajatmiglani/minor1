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
from django.conf.urls import url
from django.urls import include , path
from django.contrib import admin
from backend import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

#from backend.views import ToDoListView, ToDoDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/',views.quiz.as_view()),
    url(r'^auth/',views.authentication.as_view()),
    url(r'^quizStudents/',views.quizStudents.as_view()),
    url(r'^quizavailable/',views.quizavailable.as_view()),
    url(r'^submit_marks/',views.submit_marks.as_view()),
    url(r'^batchdetails/',views.batchdetails.as_view()),
    url(r'^session/',views.session_.as_view()),
    #path('file/',include('fileupload_rest.urls')),
    url(r'^api/', include('fileupload_rest.urls') ),
    
    

    #url(r'^api/v1/auth/',include('rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
    #url(r'^$',views.IndexView.as_view(),name='index'),
    #url(r'^$', TemplateView.as_view(template_name='backend/index.html')),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns=format_suffix_patterns(urlpatterns)