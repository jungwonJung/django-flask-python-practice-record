from django.db import models


class Addresses(models.Model):
    name = models.CharField(max_length=10)         # class 가 가지고있는 Column 을 적어줘야함 ,한글 1 자는 2byte
    phone_number = models.CharField(max_length=13)  # 앞에 0이 붙기때문에 int 로 설정하면안됨
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # 현재 시간을 기록하는 코드

    class Meta:
        ordering = ['created']
