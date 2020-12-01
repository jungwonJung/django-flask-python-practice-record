from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', ) # 생성된 데이터 목록을 리스트에서 user 과 product 만 미리보기가능

admin.site.register(Order, OrderAdmin)