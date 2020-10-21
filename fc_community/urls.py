"""fc_community URL Configuration

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
from django.urls import path, include     # 밑에 include import 해준다

urlpatterns = [
    path('admin/', admin.site.urls),  # admin 은 기본적으로 설정되어잇다  
    path('fc_user/', include('fc_user.urls'))  #fc_user  안에 있는 모든 url 들은 fc_user.urls 에서 관리하겠다 선언
]
