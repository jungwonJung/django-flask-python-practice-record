from django.db import models

# Create your models here.

# 1... 사용자명, 비밀번호, 가입시간, 클래스를 만듬 sql 에서 따로작성필요없음 sql 에서 작성도 가능함 
class Fc_user(models.Model):   # 클래스를 만들때 쟝고에서 제공하는 models.Model 상속받아야함
    username = models.CharField(max_length=32,
        verbose_name='사용자명')  # 나중에 admin 에서 username이 영문이 아니라 사용자명으로 보임
    useremail = models.EmailField(max_length=128,
        verbose_name='사용자 이메일')
    password = models.CharField(max_length=64,
        verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, # dttm 데이트타임의 약자 지금의시간이 자동입력
        verbose_name='등록시간')
# 위의 설정을 바꾸거나 추가 할때마다 1..makemigrations ,   2... migrate 해야함

    def __str__(self):
        return self.username   # 파이썬에 존재하는 내장함수 __str__ 을 사용하여 저장된 username 을 self 로 반환한다는 뜻  
# 2.... 1번의 테이블 명 을 지정해준다   makemigrations 명령어를 사용하면 migrations.0001_initial 파일 생성 그 후에 makemigrate 하면 db 에 우리가 지정한 데이터 테이블이 생긴다 모델변경시마다
    class Meta:
        db_table = 'fastcampus_fc_user'
        verbose_name = '보더콜리단'  
        verbose_name_plural = '보더콜리단'  # 쟝고에서는 기본적으로 복수형으로 나타냄 그걸 수정하기위해 plural 추가