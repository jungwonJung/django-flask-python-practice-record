"""django_s URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from user.views import index, RegisterView  # user app 폴더 밑에 views 밑에 index 파일을 가져온다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('register/', RegisterView.as_view()),  #  class를사용하는경우 as_view 를 사용
]
