# 쟝고내에서 제공되는 form 기능을 사용하기위해 forms.py 만듬

from django import forms
from .models import Fc_user
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : '아이디를 입력해주세요.'
        },
        
            max_length=32, label="사용자이름")
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
            label="비밀번호", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:                                                  # 26~29 예외처리 하는 방법
                fc_user = Fc_user.objects.get(username=username)
            except Fc_user.DoesNotExist:
                self.add_error('username', '아이디가 없습니다')
                return
            
            if not check_password(password, fc_user.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
            else:
                self.user_id = fc_user.id