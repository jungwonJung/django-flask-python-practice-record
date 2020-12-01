from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')

    def __str__(self):    
        return self.email
        
    class Meta:
        db_table = 'jung_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'   # 복수형이름도 지정해주기로한다

# 회원관리에 관한 model을 설정해준다 django 에서는 데이터필드를 만들때 사용한다
# 간단한 이메일과 비밀번호를 입력하게하면 생성일자가 추가되는순간 날짜가 기록될수있게 auto_now_add=True 사용할것임
# verbose_name = 을 설정하여 관리자 화면에서도 볼수있게 만들어준다

