# view 에 board_list 파일을 만들고나서 templates 에 board_list.html 생성 url 파일에, list/ boardlist 지정, fc community url 에 board 지정
from django.urls import path
from . import views  

urlpatterns = [
    path('detail/<int:pk>/', views.board_detail),    #views 7번라인 참조  숫자형의변수 pk
    path('list/', views.board_list),  
    path('write/', views.board_write),
]
