from django.shortcuts import render
from .models import Board  # 모델에서 만든 객체를 가져온다
# Create your views here.

def board_list(request):
    boards = Board.objects.all().order_by('-id')    # 뒤에있는 order.by 는 정렬 -id 아이디 역순
    return render(request, 'board_list.html', {'boards' : boards})   # 템플릿에 전달