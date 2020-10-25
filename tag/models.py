from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='작성시간')

def __str__(self):
    return self.name

class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = '보더콜리단 태그'  
        verbose_name_plural = '보더콜리단 태그'