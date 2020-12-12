# 가상환경세팅 후 2번째로 진행
from rest_framework import serializers 
from django.contrib.auth.models import User  # 13번 model=User 를 가져오기위해 
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed     # 인증실패 51번코드 추가
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class RegisterSerializer(serializers.ModelSerializer):  # Register serializer class 설정 
    password = serializers.CharField(max_length=64,min_length=8,write_only=True)  # models 에서는 password = models 로 했다면 serializers 는 데이터베이스에 있는 필드를 serializer 화 시키기때문에 serializer 로 시작


    class Meta:
        model = User
        fields=['username','email','password']  # models.py 에서 만든 User 클래스에서 username, email, password 를 json직렬화 (serializer화) 시켜준다

    def validate(self, attrs):   # 유효성테스트 함수 self, 속성(get,request, 등등)
        email = attrs.get('email', '')               #  이미존재하는지 vaild 코드문 여기서는 email 사용
        password = attrs.get('password', '')  
        username = attrs.get('username', '')    
        # attrs 를 사용하는 이유는 class 에서 객체 프로토콜로 class 생성작업시 번거로움을 덜어준다 request 나 get 요청 방식 들어갔음 원래는
        if not username.isalnum(): # isalnum 알파벳과 영문으로 이루어져야함
            raise serializers.ValidationError(" 이름은 영문과 숫자로 이루어져야합니다 ")  # 유효성에러 출력

        return attrs

    def create(self, validated_data):  # create 함수 선언 self def validate 에서 return attrs 된 data 를 받아서 User 라는 데이터베이스에 user를 만든다
        return User.objects.create_user(**validated_data)
        # models.py UserManeger class 에 속한 create_user 값을 반환한다 
        # validated_data 는 restframework/serializers.py 내장된 함수 사용
 
class EmailVerificationSerializer(serializers.ModelSerializer): # 이메일 인증 api 폼 생성 
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']   # User 의 token을 json 형태로 직렬화



class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=4, read_only=True)
    tokens = serializers.CharField(max_length=255, min_length=8, read_only=True)

    class Meta:
        model = User
        fields = ['email','username', 'tokens','password'] # User database 의 필드 값 사용


    def validate(self, attrs): # parameter 내용 restframework/serializers.py validate 내장함수 사용
        email = attrs.get('email', '')
        password = attrs.get('password', '')


        user = auth.authenticate(email=email, password=password)  # user 는 database auth 필드에서 입력받은 이메일과 비밀번호를 진짜가 맞는지 확인한다
        if not user:
            raise AuthenticationFailed('존재하지 않습니다. 다시 시도해주세요')  # 인증실패 에러 
        if not  user.is_active:
            raise AuthenticationFailed('계정이 비활성화 상태입니다. 관리자에게 문의하세요')
        if not  user.is_verified:
            raise AuthenticationFailed('이메일이 인증 되지 않았습니다')
            # AuthenticationFailed 라는 exceptions.py 의 class 사용한다 기본세팅이 잡혀있음

        return {                  # response 내용 
            'email' : user.email,
            'username' : user.username,
            'password' : user.password,
            'tokens' : user.tokens,
            
        }

        return super().validate(attrs)



class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length = 2)

    class Meta:
        fields = ['email']



class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length = 6, max_length = 64, write_only=True)
    token = serializers.CharField(
        min_length = 1 , write_only=True)
    uidb64 = serializers.CharField(
        min_length = 1 , write_only=True)  
    
    
    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self. attrs):
        try:
            pass
        except expression as identifier:
            pass
        return super().validate(attrs)