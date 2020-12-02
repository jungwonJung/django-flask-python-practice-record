from django import forms  # 쟝고 에서 forms 를 가져온다 
from .models import User


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

    def clean(self):
        cleaned_data = super().clean()    # data 의 유효성체크
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')   # 유효성체크가 완료된 password 데이터를 가져오겠음 
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password' ,'비밀번호가 서로다릅니다')       # 패스워드와 패스워드확인다를경우 error 메시지 출력
                self.add_error('re_password' ,'비밀번호가 서로다릅니다')
            else:
                user = User(         # User 데이터베이스에 저장
                    email=email,
                    password=password,
                )
                user.save()