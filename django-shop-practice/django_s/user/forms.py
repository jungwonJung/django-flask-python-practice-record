from django import forms  # 쟝고 에서 forms 를 가져온다
from django.contrib.auth.hashers import check_password, make_password    # 비밀번호 암호화기능 가져오기 입력받은값과 인코딩된 값을 비교해준다
from .models import User
from django.views.decorators.csrf import csrf_exempt

class RegisterForm(forms.Form):    
    email = forms.EmailField(     # RegisterForm 내의 email 은 forms의 emailfield 에러메시지중에 required 가 나오면 이메일을 입력해주세요 출력
        error_messages={
            'required' : '이메일을 입력해주세요'
        },
        max_length=64, label='이메일'   # 최대길이 64자 라벨은 이메일
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'   # PasswordInput 을 widget 으로 지정 
    )
    re_password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호 확인 ' 
    )
    @csrf_exempt
    def clean(self):
        cleaned_data = super().clean()    # data 의 유효성체크
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')   # 유효성체크가 완료된 password 데이터를 가져오겠음 
        re_password = cleaned_data.get('re_password')

        print('hello')
        if password and re_password:
            if password != re_password:
                self.add_error('password' ,'비밀번호가 서로다릅니다')       # 패스워드와 패스워드확인다를경우 error 메시지 출력
                self.add_error('re_password' ,'비밀번호가 서로다릅니다')

class LoginForm(forms.Form):    
    email = forms.EmailField(     # RegisterForm 내의 email 은 forms의 emailfield 에러메시지중에 required 가 나오면 이메일을 입력해주세요 출력
        error_messages={
            'required' : '이메일을 입력해주세요'
        },
        max_length=64, label='이메일'   # 최대길이 64자 라벨은 이메일
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'   # PasswordInput 을 widget 으로 지정 
    )
    @csrf_exempt
    def clean(self):
        cleaned_data = super().clean()    # data 의 유효성체크
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')   # 유효성체크가 완료된 password 데이터를 가져오겠음 

        if email and password:
            try:
               user = User.objects.get(email=email)  # User 의 데이터베이스에 저장된 email 이 요청받은 email 과 동일한지 확인
            except User.DoesNotExist:      # User 데이터베이스와 동일하지 않다면
               self.add_error('email','존재하지않는 이메일 입니다!')
               return
            
            if not check_password(password, user.password):   
                self.add_error('password', '비밀번호를 틀렸습니다')