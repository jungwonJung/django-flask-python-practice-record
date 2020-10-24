from django.db import models

# Create your models here. 게시판의 모델을 설정해줘야함

class Board(models.Model): #Board 라는 클래스 설정
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fc_user.Fc_user', on_delete=models.CASCADE,  # 사용자 정보가 삭제되면 ForeignKey 가 가르키고 있는 값을 같이 삭제하겟다
                                verbose_name='작성자')       
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='작성시간')

def __str__(self):
    return self.title

class Meta:
        db_table = 'fastcampus_fc_user'
        verbose_name = '보더콜리단 게시글'  
        verbose_name_plural = '보더콜리단 게시글'