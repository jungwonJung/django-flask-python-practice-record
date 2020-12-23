from django.http import JsonResponse
from django.views import View  # django views 의 최상위 View 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.validators import validate_email, ValidationError
from django.contrib.auth import authenticate, login


class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data' : data,
            'message' : message,
        }

        return JsonResponse(result, status)


class UserCreateView(BaseView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해주세요', status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='비밀번호를 입력해주세요', status=400)
        email = request.POST.get('email', '')
        try:
            validate_email(email)
        except ValidationError:
            self.response(message='이메일을 입력해주세요', status=400)
        
        try: # 예외처리 기본 try문에서 에러가날경우 except 동작
            user = User.objects.create_user(username, password, email)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디입니다.', status=400)

        return self.response({'user.id' : user.id})



class UserLoginView(BaseView):
    def post(self, request):
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해주세요', status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='올바른 비밀번호를 입력해주세요', status=400)
        user = authenticate(request, usernmame=username, password=password) # 1. django 에서 기본제공해주는 authenticate 에서 username 과 password 일치하는데이터값이 있는지 확인
        if user is None: # 2.없다면  None 을 반환해준다 
            return self.response(message='입력정보를 확인해주세요', status=400)
        login(request, user)

        return self.response


class UserLogoutView(BaseView):
    def get(self, request):
        
