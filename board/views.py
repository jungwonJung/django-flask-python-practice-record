from django.shortcuts import render, redirect
from .models import Board  # 모델에서 만든 객체를 가져온다
from .forms import BoardForm
from fc_user.models import Fc_user

 
def board_detail(request, pk):   #주소로부터 뒤에붙은 글의 순서별로 설정하려면 pk 를 추가한다 url에서 연결
    board = Board.objects.get(pk=pk)
    return render(request, 'board_detail.html',{'board' : board})



def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fc_user = Fc_user.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fc_user
            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()
     
    return render(request, 'board_write.html', {'form' : form })



def board_list(request):
    boards = Board.objects.all().order_by('-id')    # 뒤에있는 order.by 는 정렬 -id 아이디 역순
    return render(request, 'board_list.html', {'boards' : boards})   # 템플릿에 전달