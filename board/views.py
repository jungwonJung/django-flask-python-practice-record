from django.shortcuts import render, redirect
from .models import Board  # 모델에서 만든 객체를 가져온다
from django.http import Http404
from .forms import BoardForm
from fc_user.models import Fc_user
from django.core.paginator import Paginator     # 페이징 제공 django 안에잇음
from tag.models import Tag

 
def board_detail(request, pk):   #주소로부터 뒤에붙은 글의 순서별로 설정하려면 pk 를 추가한다 url에서 연결
    try:
        board = Board.objects.get(pk=pk)        #  없는 게시글 넘버를 입력하여 주소로 입력할경우 예외 처리 추가
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을수없습니다.')
    
    
    return render(request, 'board_detail.html',{'board' : board})



def board_write(request):
    if not request.session.get('user'):   # request.session 에 get('user') 유저가 없으면 
        return redirect('/fc_user/login')  # 로그인 페이지로 보내준다  (주소치고 들어가면 로그인창으로 보내버림 )


    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fc_user = Fc_user.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fc_user
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, created  = Tag.objects.get_or_create(name=tag)   #name=tag 가 일치하는 값이 있으면 가져오고 없으면 생성해서 가져옴 
                board.tags.add(_tag)  # board 가 생성되면 id 값이 생성됨 pk 값 이 먼저 생성이되어야 tag 값이 추가가됨 순서가 바뀌면 에러가 남 선 board 후 태그

           

            return redirect('/board/list/')
    else:
        form = BoardForm()
     
    return render(request, 'board_write.html', {'form' : form })



def board_list(request):
    all_boards = Board.objects.all().order_by('-id')    # 뒤에있는 order.by 는 정렬 -id 아이디 역순
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 2)   # paginator 를 만들고 (전체오브젝트수, 한페이지당 보여줄개수)


    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards' : boards})   # 템플릿에 전달