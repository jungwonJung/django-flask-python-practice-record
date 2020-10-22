from django.http import HttpResponse
from django.shortcuts import render, redirect    # redirect 를사용하기위해 추가
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호 암호화를 하기위한 import
from .models import Fc_user  # fc유저 생성을위해 models 안에있는 Fc_user 클래스 값을 가져와야함

# Create your views here.

# 4...작업한 register 템플릿안에있는 폴더를 파이썬하고 연결하는순서  하고나서 url 설정
# request 를 꼭 적고 반환하고 싶은 html(함수) 을 적어야함
# get 방식과 post 방식을 분기해줌

def home(request):
    user_id = request.session.get('user')

    if user_id:
        fc_user = Fc_user.objects.get(pk=user_id)
        return HttpResponse(fc_user.username)
    return HttpResponse('Home!')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다!'
        else: 
            fc_user = Fc_user.objects.get(username=username)    # Fc_user 내에 object 안에 get 이란 함수를 사용 모델 안에 필드명 username 
            
            # login 내에 비밀번호일치하는지 확인
            if check_password(password, fc_user.password):    
                # 비밀번호가 일치. 로그인 처리를!  아무code 도 넣지않으면 에러 발생
                
                request.session['user'] = fc_user.id   # request.session 내에 user 라는 키의 값이 각 세션 아이디별로 쿠키value 다름 
                return redirect('/')
            else:
                 res_data['error'] = '비밀번호가 다릅니다!!'
        
        
        return render(request, 'login.html', res_data)   # 에러를 띄우기위해 render 에 res_data 추가

def register(request): 
    if request.method == 'GET':
         return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)   # 네임필드 앞에 있는 값을 키로 저장됨,  예외처리 request.POST (dict type) 키가 없으면 에러가 생김 POST.GET추가시 []를 () 로 변경
        password = request.POST.get('password', None)  # 빈문자열이 들어오거나 값이 없을때 23번 코드 실행
        re_password = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)

        # if password != re_password:
        #     return HttpResponse('비밀번호가 다릅니다!')  요롷게도 할수있지만 페이지에서 머무르고 에러메시지를 확인할수있게 개선하고 render 에 값추가
        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다!'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            fc_user = Fc_user(             # 클래스 변수 객체 하나를 생성함
                username=username,
                useremail=useremail,
                password=make_password(password)
        )

            fc_user.save()   # 저장해주기
        return render(request, 'register.html', res_data)  # 저장하고 나서 register 페이지를 리턴 반환해줫기 때문에 페이지 이동없이 그대로
                                                           # res_data 를 register.html 에서 보여주라고 했기때문에 에러 메시지를 보여주는 기능을 제작해야함