from django.contrib import admin
from .models import Fc_user  # models 안에  (.models ) 있는 Fc_user   class 를 가져 오겠음

# Register your models here. 


class Fc_userAdmin(admin.ModelAdmin):  # pass 는 아무것도 안하고 빈 class 를 만들겠닺는 뜻
    list_display = ('username', 'password')   # admin 창내에서 미리보고 싶을때 설정   field 들이 객체화 되서 보임
    
admin.site.register(Fc_user, Fc_userAdmin)