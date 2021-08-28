from django.contrib import admin
from .models import User # user.models.User 를 토대로 admin class 생성
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )  # modles.py/User 에 있는 email  &&주의사항 ('email', ) 안에 , 를안찍으면 튜플로 인식을못함 필히 , 를찍어 튜플로 인식하게해야함
                                # 생성된 데이터 목록을 리스트에서 email 만 미리보기가능
admin.site.register(User, UserAdmin)