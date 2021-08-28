from django.shortcuts import redirect
from .models import User



def login_required(function):
    def wrap(request, *args, **kwargs):  # wrap 한 함수와 기존함수의 인자값을 맞춰줘야함 안그러면 wrap 에러 발생\
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)
    
    return wrap

# 여기에 @login_required 처럼 가능하긴하지만 현재는 사용안함
def admin_required(function):
    def wrap(request, *args, **kwargs):  
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = User.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')

        return function(request, *args, **kwargs)
    
    return wrap

