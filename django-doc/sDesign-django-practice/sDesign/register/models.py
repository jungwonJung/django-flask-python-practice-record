from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
class UserManger(BaseUserManager):  

    def create_user(self,username,email,password=None):

        if username is None:
            raise TypeError("이름을 입력해주세요")
        if email is None:
            raise TypeError("이메일을 입력해주세요")

        user=self.model(username=username,email=self.normalize_email(email)) # normalize_email 기본이메일형태
        user.set_password(password)  # 현재암호화 진행안함 비밀번호 암호화
        user.save()
        return user     # post 를 보내면 user를 json 형태로 다시 보여기위해 추가

    def create_superuser(self,username,email,password=None):

        if password is None:
            raise TypeError("비밀번호를 입력해주세요")
        
        user=self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user 

class User(AbstractBaseUser, PermissionsMixin):   
    username = models.CharField(max_length=255,unique=True, db_index=True)
    email = models.EmailField(max_length=255,unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)  # 이메일 인증된 경우 python shell 통하여 인증이 되었는지 Boolean 으로 표현 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# """
# User 라는 class 를 만들어요 User 라는 데이터베이스를 만들어서 그 데이터베이스파일 안에 schema를 설정해주는과정입니다
# username 은 models에 캐릭터필드로 최대길이는 255자 유니크필드로 db에서 index도 설정해줄거에요
# email 도 위의 username과 설정값은 동일해요
# is_veryfied 만약에 이메일인증을 받았는지를 확인해줄거에요 boolean 필드로 기본값은 False로 할거에요 
#  만약 True 로 한다면 모든 이미 인증이되었다고 인식할테니깐 이메일인증을하는이유가없어지겟죠
#  이메일인증을 했다면 활성화를 해야하는데 is_active 는 활성화를 여부를 설정해줘요  
#  is_staff 만약 생성된 값중에 이 웹서비스를 관리하거나 관계자일경우 설정해주기위해 만들어요 기본값은 False 로해야만 모든 값이 관리자가 아닐겁니다
#  created_at 은 생성된 데이터의 생성된 시간을 표시하기위해 만듭니다 auto_now_Add 를 True 로 설정해주면
#  데이터가 추가될때의 시각이 자동저장됩니다
#  updated_at 은 데이터의 값이 수정이 이뤄질때 수정된시간을 표시하기위해 만듭니다 auto_now 로 한다면 수정되는 그시점의 시간으로 변경될겁니다
# """
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usename']

    objects = UserManger()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token) ,
        }