# fc_user.url 관리해주기로 했음에 fc_user 밑에 urls.py 생성 
from django.urls import path
from . import views   # views 파일을 사용하기위해 import 한다

urlpatterns = [
    path('register/', views.register),  # view 파일 안에있는 register  라는 함수사용
    path('login/', views.login),
    path('logout', views.logout),
]
