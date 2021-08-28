from django.shortcuts import render, redirect
from django.views.generic.edit import FormView  # django.views 안에 generic.edit 안에 FormView 기능 가져오겠음
from .forms import RegisterForm, LoginForm   # user.forms 안에 RegisterForm 가져오겠음둥
from django.contrib.auth.hashers import make_password 
from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html', { 'email' : request.session.get('user')})  # index 가 request 받으면 index.html 로 렌더링해준다
                                                                                    # 세션에 저장된 email 주소를 index.html 로 반환


class RegisterView(FormView):           
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = User(
            email = form.data.get('email'),
            password = make_password(form.data.get('password')),
            level='user'
        )
        user.save()

        return super().form_valid(form)

class LoginView(FormView):           
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form): # 유효성검사가 다 끝났을때 들어오는 함수
        self.request.session['user'] = form.data.get('email')  # 로그인한 사용자의 email 을 세션에 저장하겠음

        return super().form_valid(form)  # super 함수를 사용하여 form_valid 함수 호출


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')