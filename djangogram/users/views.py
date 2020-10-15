from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def main(request):
    if request.method == 'GET':
        return render(request, 'users\main.html')
    # 장고 문서 내에 존재하는 장고 로그인폼 사용  겟방식과 포스트 분기 코드 작성
    elif request.method == 'POST':  
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('posts:index'))

            else:
                # Return an 'invalid login' error message.
                return render(request, 'users\main.html')
# 장고폼사용 회원가입 로직 
def signup(request):
    if request.method == 'GET':
        form = SignUpForm()

        return render(request, 'users/signup.html', {'form' : form})

    elif request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
#자동로그인 성공하면 cleaned 데이터에 저장됨
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('posts:index'))

            else:
                # Return an 'invalid login' error message.
                return render(request, 'users\main.html')

        return render(request, 'users/main.html')