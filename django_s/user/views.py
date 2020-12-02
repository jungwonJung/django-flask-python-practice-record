from django.shortcuts import render
from django.views.generic.edit import FormView  # django.views 안에 generic.edit 안에 FormView 기능 가져오겠음
from .forms import RegisterForm    # user.forms 안에 RegisterForm 가져오겠음둥

# Create your views here.

def index(request):
    return render(request, 'index.html')  # index 가 request 받으면 index.html 로 렌더링해준다


class RegisterView(FormView):           
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'